import cv2
import time
import numpy as np
import os
import argparse
from datetime import datetime
import shutil

def show_webcam(args, mirror=False):
  frequency = 100 # Hertz
  duration  = 50 # milliseconds
  cam = cv2.VideoCapture(0)
  time.sleep(0.5)
  start_time = time.time()
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
      timestamp = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f')[:-3]
      timestamp = timestamp + '.jpg'
      image_filename = os.path.join(args.image_folder, timestamp)
      print(image_filename)
      if args.image_folder != '':
        cv2.imwrite(image_filename, img)
      start_time = time.time()
    key = np.int16(cv2.waitKey(1))
    if key == 27:
      break  # esc to quit
  cv2.destroyAllWindows()

def main():
  show_webcam(args, mirror=True)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Garra Robotica')
  parser.add_argument(
    'image_folder',
    type=str,
    nargs='?',
    default='',
    help='Path to image folder. This is where the images from the run will be saved.'
    )
  args = parser.parse_args()
  if args.image_folder != '':
    print("Creating image folder at {}".format(args.image_folder))
    if not os.path.exists(args.image_folder):
      os.makedirs(args.image_folder)
    else:
      shutil.rmtree(args.image_folder)
      os.makedirs(args.image_folder)
    print("RECORDING THIS RUN ...")
  else:
    print("NOT RECORDING THIS RUN ...")
  main()

