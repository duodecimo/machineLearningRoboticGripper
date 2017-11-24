# machineLearningRoboticGripper

This project uses gestures to control a robotic gripper.
The gestures are captured by a webcam. They are classifyed into basic commands and then transmitted via USB to a Arduino board, that translates them into action.
The gestures are trainned by a deep learning neural network.
The resulting model is used to predict the meaning of a gesture.

## Materials

To be able to run this project, users will definitely need some materials (or equivalent stuff): 
  - Arduino prototyping board (i.e. Uno, Leonardo, etc)
  - USB cable for the Arduino board.
  - protoboard
  - bunch of jumpers. (at least 16)
  - Robotic gripper with 4 servos (movements: left, right, foward, back, up, down, grip, loose).
  - External font with 5 volts and 2.5A output.
  - Desktop computer (at least i3 5th generation or equivalent)
  - External webcam (a decent one)

## Installation

Users are invited to install [anaconda](https://conda.io/docs/user-guide/install/index.htm).
Then, they can create an environment (if you are new to python/anaconda, you can learn about it [here](https://conda.io/docs/user-guide/tasks/manage-environments.html) ).
The environment may be created using the file **duo_ml.yml**, that can be obtainned on the root of this project.
Once again, if you a re new to anaconda you can learn how to create an environment from a file [here](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file).
this should be enough to run the project python code.

Users should install also a [Arduino IDE](https://www.arduino.cc/en/Main/Software).

Finally, the user should clone this repository (if someone is reading this here, at least must know github. There are instructions on github site how to clone a project).

## Knowing what to expect

There is a very rudimentary video of the project working on youtube (portuguese spoken, but even if you do not speak portuguese, the visual is there). You can watch it [here](https://youtu.be/2g8e_4U-850).
