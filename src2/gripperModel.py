import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras.layers import Lambda, Conv2D, MaxPooling2D, Dropout, Dense, Flatten
from utils import INPUT_SHAPE, batch_generator
import argparse
import os
import cv2
import sys

np.random.seed(0)

def load_images_from_folder(folder, result, images, results):
    print('folder: ', folder)
    for filename in os.listdir(folder):
      img = os.path.join(folder,filename)
      if img is not None:
        images.append(img)
        results.append(result)
    return images, results

def load_data(args):
  images = []
  results =[]
  labels = ['nothing', 'left', 'right', 'grip', 'loose', 'up', 'down', 'foward', 'back']
  #load a list of images and a corresponding list of results (images=640x480)
  for counter in range(0,8):
    folder = os.path.join(args.capture_dir, labels[counter])
    images, results = load_images_from_folder(folder, counter, images, results)
  #load a list of images and a corresponding list of results (images=640x480)
  #images, results = load_images_from_folder('capt2/nothing/', 0, images, results)
  #images, results = load_images_from_folder('capt2/left/', 1, images, results)
  #images, results = load_images_from_folder('capt2/right/', 2, images, results)
  #images, results = load_images_from_folder('capt2/grip/', 3, images, results)
  #images, results = load_images_from_folder('capt2/loose/', 4, images, results)
  #images, results = load_images_from_folder('capt2/up/', 5, images, results)
  #images, results = load_images_from_folder('capt2/down/', 6, images, results)
  #images, results = load_images_from_folder('capt2/front/', 7, images, results)
  #images, results = load_images_from_folder('capt2/back/', 8, images, results)
      
  print("Images: ", len(images))
  print("Results: ", len(results))
  print("labels: ", len(labels), labels)

  X_train, X_valid, y_train, y_valid = train_test_split(images, results, test_size=0.2, shuffle = True, random_state=0)

  print("Train Images: ", len(X_train))
  print("Valid Images: ", len(X_valid))
  print("Train Results: ", len(y_train))
  print("Valid Results: ", len(y_valid))

  # if we wish to check some of the images, just change de index value
  # note that the index can't be bigger than the number of images -1
  checkIndex = 40
  cv2.imshow('Capture', cv2.imread(X_train[checkIndex]))
  print(X_train[checkIndex])
  print(labels[y_train[checkIndex]])
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  sys.exit(0)

  return X_train, X_valid, y_train, y_valid

def build_model(args):
    """
    Modified NVIDIA model
    """
    model = Sequential()
    model.add(Lambda(lambda x: x/127.5-1.0, input_shape=INPUT_SHAPE))
    model.add(Conv2D(24, 5, 5, activation='elu', subsample=(2, 2)))
    model.add(Conv2D(36, 5, 5, activation='elu', subsample=(2, 2)))
    model.add(Conv2D(48, 5, 5, activation='elu', subsample=(2, 2)))
    model.add(Conv2D(64, 3, 3, activation='elu'))
    model.add(Conv2D(64, 3, 3, activation='elu'))
    model.add(Dropout(args.keep_prob))
    model.add(Flatten())
    model.add(Dense(100, activation='elu'))
    model.add(Dense(50, activation='elu'))
    model.add(Dense(10, activation='elu'))
    model.add(Dense(1))
    model.summary()

    return model


def train_model(model, args, X_train, X_valid, y_train, y_valid):
    """
    Train the model
    """
    checkpoint = ModelCheckpoint('model-{epoch:03d}.h5',
                                 monitor='val_loss',
                                 verbose=0,
                                 save_best_only=args.save_best_only,
                                 mode='auto')

    model.compile(loss='mean_squared_error', optimizer=Adam(lr=args.learning_rate))
    
    model.fit_generator(batch_generator(X_train, y_train, args.batch_size, True),
                        args.samples_per_epoch,
                        args.nb_epoch,
                        max_q_size=1,
                        validation_data = batch_generator(X_valid, y_valid, args.batch_size, False),
                        nb_val_samples=len(X_valid),
                        callbacks=[checkpoint],
                        verbose=1)


def s2b(s):
    """
    Converts a string to boolean value
    """
    s = s.lower()
    return s == 'true' or s == 'yes' or s == 'y' or s == '1'


def main():
    """
    Load train/validation data set and train the model
    """
    parser = argparse.ArgumentParser(description='Behavioral Cloning Training Program')
    parser.add_argument('-d', help='capture directory',        dest='capture_dir',          type=str,   default='capture')
    parser.add_argument('-t', help='test size fraction',    dest='test_size',         type=float, default=0.2)
    parser.add_argument('-k', help='drop out probability',  dest='keep_prob',         type=float, default=0.5)
    parser.add_argument('-n', help='number of epochs',      dest='nb_epoch',          type=int,   default=10)
    parser.add_argument('-s', help='samples per epoch',     dest='samples_per_epoch', type=int,   default=20000)
    parser.add_argument('-b', help='batch size',            dest='batch_size',        type=int,   default=40)
    parser.add_argument('-o', help='save best models only', dest='save_best_only',    type=s2b,   default='true')
    parser.add_argument('-l', help='learning rate',         dest='learning_rate',     type=float, default=1.0e-4)
    args = parser.parse_args()

    print('-' * 30)
    print('Parameters')
    print('-' * 30)
    for key, value in vars(args).items():
        print('{:<20} := {}'.format(key, value))
    print('-' * 30)

    data = load_data(args)
    model = build_model(args)
    train_model(model, args, *data)


if __name__ == '__main__':
    main()

