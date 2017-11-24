# machineLearningRoboticGripper

This project uses gestures to control a robotic gripper.
The gestures are captured by a webcam. They are classifyed into basic commands and then transmitted via USB to a Arduino board, that translates them into action.
The gestures are trainned by a deep learning neural network.
The resulting model is used to predict the meaning of a gesture.

## Materials

To be able to run this project, users will definitely need some materials (or equivalent stuff): 
  - Arduino prototyping board (i.e. Uno, Leonardo, etc)
  - A USB cable for the Arduino board.
  - A protoboard
  - A bunch of jumpers. (at least 16)
  - A robotic gripper with 4 servos (movements: left, right, foward, back, up, down, grip, loose).

## Installation

Users are invited to install [anaconda](https://conda.io/docs/user-guide/install/index.htm).
Then, they can create an environment (if you are new to python/anaconda, you can learn about it [here](https://conda.io/docs/user-guide/tasks/manage-environments.html) ).
The environment may be created using the file **duo_ml.yml**, that can be obtainned on the root of this project.
Once again, if you a re new to anaconda you can learn how to create an environment from a file [here](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file).
this should be enough to run the project python code.

Users should install also a [Arduino IDE](https://www.arduino.cc/en/Main/Software).
