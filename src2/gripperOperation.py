import cv2
import time
import numpy as np
import os
import argparse
from datetime import datetime
import shutil
import serial
import time

from keras.models import load_model

import utils

def startOperation(args, mirror=False):
  #start serial
  if args.serial != '':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    print('Serial connection: ', ser.name)

  #start the camera
  frequency = 100 # Hertz
  duration  = 50 # milliseconds
  cam = cv2.VideoCapture(0)
  time.sleep(0.5)
  start_time = time.time()
  #start capture
  while True:
    ret_val, img = cam.read()
    if mirror: 
      img = cv2.flip(img, 1)
    cv2.imshow('my webcam', img)
    elapsed_time = time.time() - start_time
    if elapsed_time > 4:
      os.system('play -n synth %s sin %s' % (duration/1000, frequency))
      cv2.waitKey(1)
      ret_val, img = cam.read()
      if mirror: 
        img = cv2.flip(img, 1)
      cv2.imshow('my webcam', img)
      # predict
      predict(args, ser, img)
      start_time = time.time()
    key = np.int16(cv2.waitKey(1))
    if key == 27:
      break  # esc to quit
  cv2.destroyAllWindows()


def predict(args, ser, image):
    # The current image of gesture
    gc = ' '
    gi = 0
    labels = ['nothing', 'left', 'right', 'grip', 'loose', 'up', 'down', 'foward', 'back']

    try:
        image = utils.preprocess(image) # apply the preprocessing
        image = np.array([image])       # the model expects 4D array
        # predict the gesture
        gesture = float(model.predict(image, batch_size=1))
        print('gesture prediction: ', round(gesture), ' <- ', gesture)
        if(gesture <= 0.8):
          gc = 'n'; gi = 0;
        elif(gesture <= 1.8):
          gc = 'l'; gi = 1;
        elif(gesture <= 2.8):
          gc = 'r'; gi = 2;
        elif(gesture <= 3.8):
          gc = 'g'; gi = 3;
        elif(gesture <= 4.8):
          gc = 'o'; gi = 4;
        elif(gesture <= 7.8):
          gc = 'u'; gi = 5;
        elif(gesture <= 8.8):
          gc = 'd'; gi = 6;
        elif(gesture <= 5.8):
          gc = 'f'; gi = 7;
        elif(gesture <= 6.8):
          gc = 'b'; gi = 8;
        if(gesture != ' '):
          print('gesture: ', gc, ' - ', labels[gi])
          #ser.write(bytes(chr(gc), 'utf-8'))
          if args.serial != '':
            ser.write(bytes(gc, 'utf-8'))
          time.sleep(.02)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remote Driving')
    parser.add_argument(
        'model',
        type=str,
        help='Path to model h5 file. Model should be on the same path.'
    )
    parser.add_argument(
        'serial',
        type=str,
        default = '',
        help='Path to arduino serial, example: /dev/ttyACM0 .'
    )
    args = parser.parse_args()

    model = load_model(args.model)

    startOperation(args, mirror=false)

