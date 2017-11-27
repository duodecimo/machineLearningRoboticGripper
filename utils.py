import cv2, os
import numpy as np
import matplotlib.image as mpimg
import random
from keras.utils import np_utils


#IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS = 66, 200, 3
#IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS = 480, 640, 3
IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS = 120, 160, 3
INPUT_SHAPE = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)


def load_image(image_file):
    """
    Load RGB images from a file
    return numpy array
    """
    imgread = cv2.imread(image_file)
    return imgread

def crop(image):
    """
    Crop the image (removing the sky at the top and the car front at the bottom)
    """
    return image[60:-25, :, :] # remove the sky and the car front


def resize(image):
    """
    Resize the image to the input shape used by the network model
    """
    return cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT), cv2.INTER_AREA)


def rgb2yuv(image):
    """
    Convert the image from RGB to YUV (This is what the NVIDIA model does)
    """
    return cv2.cvtColor(image, cv2.COLOR_RGB2YUV)


def preprocess(image):
    """
    Combine all preprocess functions into one
    """
    #image = crop(image)
    image = resize(image)
    image = rgb2yuv(image)
    return image

def random_shadow(image):
    """
    Generates and adds random shadow
    correction, see https://github.com/llSourcell/How_to_simulate_a_self_driving_car/issues/7
    """
    # (x1, y1) and (x2, y2) forms a line
    # xm, ym gives all the locations of the image
    height, width = image.shape[:2]

    x1, y1 = int(width * np.random.rand()), 0
    x2, y2 = int(width * np.random.rand()), height
    xm, ym = np.mgrid[0:height, 0:width]
    x1, y1 = IMAGE_WIDTH * np.random.rand(), 0

    # mathematically speaking, we want to set 1 below the line and zero otherwise
    # Our coordinate is up side down.  So, the above the line: 
    # (ym-y1)/(xm-x1) > (y2-y1)/(x2-x1)
    # as x2 == x1 causes zero-division problem, we'll write it in the below form:
    # (ym-y1)*(x2-x1) - (y2-y1)*(xm-x1) > 0
    mask = np.zeros_like(image[:, :, 1])
    mask[(ym - y1) * (x2 - x1) - (y2 - y1) * (xm - x1) > 0] = 1

    # choose which side should have shadow and adjust saturation
    cond = mask == np.random.randint(2)
    s_ratio = np.random.uniform(low=0.2, high=0.5)

    # adjust Saturation in HLS(Hue, Light, Saturation)
    hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
    hls[:, :, 1][cond] = hls[:, :, 1][cond] * s_ratio
    return cv2.cvtColor(hls, cv2.COLOR_HLS2RGB)


def random_brightness(image):
    """
    Randomly adjust brightness of the image.
    """
    # HSV (Hue, Saturation, Value) is also called HSB ('B' for Brightness).
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    ratio = 1.0 + 0.4 * (np.random.rand() - 0.5)
    hsv[:,:,2] =  hsv[:,:,2] * ratio
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)


def augument(imagePath, range_x=100, range_y=10):
    """
    Generate an augumented image and adjust steering angle.
    (The steering angle is associated with the center image)
    """
    image = load_image(imagePath)
    image = random_shadow(image)
    image = random_brightness(image)
    return image


def batch_generator(image_paths, ground_truths, batch_size, is_training):
    """
    Generate training image give image paths and associated steering angles
    """
    images = np.empty([batch_size, IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS])
    truths = np.empty(batch_size)
    while True:
        i = 0
        #for index in np.random.permutation(image_paths.shape[0]):
        #shuffle the two lists
        c = list(zip(image_paths, ground_truths))
        random.shuffle(c)
        image_paths, ground_truths = zip(*c)
        for index in range(len(image_paths)):
            ground_truth = ground_truths[index]
            # argumentation
            #if is_training and np.random.rand() < 0.6:
            if is_training and np.random.rand() < 0.4:
                image = augument(image_paths[index])
            else:
                image = load_image(image_paths[index]) 
            # add the image and steering angle to the batch
            images[i] = preprocess(image)
            truths[i] = ground_truth
            i += 1
            if i == batch_size:
                break
        #yield images, truths
        yield images, np_utils.to_categorical(truths, 9)

