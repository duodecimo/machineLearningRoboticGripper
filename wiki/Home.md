# Machine Learning Robotic Gripper


This project uses gestures to control a robotic gripper.
The gestures may be captured by an webcam. Other image sources, like an android phone, may be used as well. Captured gestures are classified into basic commands and then transmitted via USB to an Arduino board, that translates them into action.
The gestures are trainned by a deep learning neural network.
The resulting model is used to predict the meaning of a gesture.

## Materials

To be able to run the full project, users will definitely need some materials (or equivalent stuff): 
  - Arduino prototyping board (i.e. Uno, Leonardo, etc)
  - USB cable for the Arduino board.
  - protoboard
  - bunch of jumpers. (at least 16)
  - Robotic gripper with 4 servos (movements: left, right, foward, back, up, down, grip, loose).
  - External power source with 5 volts and 2.5A output.
  - Desktop computer (at least i3 5th generation or equivalent)
  - External webcam (a decent one)

### a visual guide to project materials

|material|image|
|------|-----------------------------|
|Arduino Uno | <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/arduinoUno.jpg" width="200"> |
|Arduino USB cable| <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/usbCable.jpg" width="200"> |
|protoboard | <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/protoboard.jpg" width="200"> |
|jumpers | <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/jumpers.jpg" width="200"> |
|robotic gripper | <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/roboticGripper.jpg" width="200"> |
|power source | <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/powersource.jpg" width="200"> |
|desktop computer | <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/roboticGripperWebcam.jpg" width="200"> |
|webcam | <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/webcam.jpg" width="200"> |

## Installation

Users are invited to install [anaconda](https://conda.io/docs/user-guide/install/index.htm). The python 3.x version is recomended, as the python code used is for version 3, and there are sure some differences from python 2.x code. I belive that the code may be adapted to python 2.x, but this may demand a lot of work.

With anaconda installed, they can create an environment (if you are new to python/anaconda, you can learn about it [here](https://conda.io/docs/user-guide/tasks/manage-environments.html) ).
The environment may be created using the file **duo_ml.yml**, that can be obtainned on the root of this project.
Once again, if you are new to anaconda you can learn how to create an environment from a file [here](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file). Note that by creating and then using the environment will install all nescessary code packages needed in the correct (original used) versions. So, any attempt to directly install code packages may broke the code here.
this should be enough to run the project python code.

Users should install also an [Arduino IDE](https://www.arduino.cc/en/Main/Software).

Finally, users should clone this repository (if someone is reading this here, at least must know github. There are instructions on github site how to clone a project).

## Knowing what to expect

There is a very rudimentary video of the project working on youtube (portuguese spoken, but even if you do not speak portuguese, the visual is there). You can watch it [here](https://youtu.be/2g8e_4U-850).

## Getting the job done

As an early version, the [jupyter notebook](http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb) **roboticGripper.ipynb**, that can be obtainned on the root directory of this repository, (it may be soon transfered to an inner backup folder) has a complete code implementing the full project.

It is all at an early stage, so, there sure is a lot of room for improvements.

Now we use 3 notebooks, each one executes one phase of the project, and they can be found at the root directory of this repository:
-  **01_captureAndSaveGestures_roboticGripper.ipynb**
-  **02_trainModel_roboticGripper.ipynb**
-  **03_operation_roboticGripper.ipynb**

After all, the project demands at least 3 phases:

- Capture the gestures (with values) to future use in supervised learning.
- Train a model using deep learning neural network buid with [Keras/TensorFlow](https://keras.io/).
- Use the model predicted commands to operate the robotic gripper.

Have fun!

©Duodécimo, December, 2017.
