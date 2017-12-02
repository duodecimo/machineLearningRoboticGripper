# Garra Robótica com Aprendizagem de Máquina


Este projeto usa gestos para controlar uma garra robótica.
Os gestos podem ser capturados por uma câmera web. Outras formas de obter imagens, como um telefone android, podem eventualmente ser utilizadas também. Os gestos capturados são classificados em comandos básicos, e então transmitidos para uma placa de prototipagem Arduino via serial USB, e finalmente traduzidos em ações.
O reconhecimento de gestos é treinado por uma rede neural de aprendizagem profunda (_deep learning_).
O modelo resultante é utilizado para prever o significado de um gesto.

## Materiais

Para executar a totalidade deste projeto, os usuários vão, sem sombra de dúvidas, precisar de alguns materiais (ou peças equivalentes):
  - placa de prototipagem Arduino (por exemplo Uno, Leonardo, etc)
  - cabo USB para a placa Arduino.
  - placa de prototipagem (_protoboard_).
  - alguns _jumpers_ M-M. (pelo menos uns 16)
  - Garra robótica completa com 4 servo motores (movimentos: esquerda, direita, frente, trás, acima, abaixo, pegar, largar).
  - Fonte de alimentação externa com saída de 5 volts e 2,5 amperes.
  - Computador de mesa (com pelo menos um i3 de 5ª geração ou equivalente)
  - Câmera web externa (que seja decente)

### um guia visual para os materiais do projeto

|material|imagem|
|------|-----------------------------|
|Arduino Uno | <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/arduinoUno.jpg" width="200"> |
|cabo USB Arduino| <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/usbCable.jpg" width="200"> |
|placa de prototipagem| <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/protoboard.jpg" width="200"> |
|jumpers| <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/jumpers.jpg" width="200"> |
|garra robótica| <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/roboticGripper.jpg" width="200"> |
|fonte externa| <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/powersource.jpg" width="200"> |
|computador| <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/roboticGripperWebcam.jpg" width="200"> |
|câmera web| <img src="https://github.com/duodecimo/machineLearningRoboticGripper/blob/master/images/webcam.jpg" width="200"> |

## Instalação

Os usuários são incentivados a instalar o [anaconda](https://conda.io/docs/user-guide/install/index.htm). A versão com python 3.x é a recomendada, pois o código python utilizado é para a versão 3, e com certeza existem diferenças para o código do python 2.x. Eu acredito que o código pode ser adaptado para python 2.x, mas isto com certeza exige um trabalho considerável.

Com anaconda instalado, pode ser criado um ambiente (_environment_) (se você é iniciante em python/anaconda, pode aprender sobre eles [aqui](https://conda.io/docs/user-guide/tasks/manage-environments.html) ).
O ambiente (_environment_) pode ser criado utilizando o arquivo **duo_ml.yml**, que pode ser obtido na raiz deste repositório.

Mais uma vez, se você é iniciante em anaconda pode aprender como criar um ambiente (_environment_) a partir de um arquivo [aqui](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file). Note que ao criar e depois utilizar o ambiente vai instalar todos os pacotes de código nas versões corretas (ou seja, as utilizadas originalmente). Portanto, qualquer tentativa de instalar diretamente pacotes de código pode quebrar o código do projeto.
Isto deve ser suficiente para rodar o código python do projeto.

Os usuários devem instalar também um [Arduino IDE](https://www.arduino.cc/en/Main/Software).

Finalmente, os usuários devem clonar este repositório (alguém lendo este documento, deve pelo menos conhecer algo sobre _github_. Existem instruções no _site github_ sobre como clonar um projeto).

## Saiba o que esperar

Existe um vídeo bastante rudimentar do projeto em ação no youtube. Você pode assisti-lo [aqui](https://youtu.be/2g8e_4U-850).

## Pondo a mão na massa

São utilizados três cadernos jupyter [(_jupyter notebook_)](http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb), cada um executando uma das fases do projeto, e que podem ser obtidos no diretório raiz deste repositório:
-  **01_captureAndSaveGestures_roboticGripper.ipynb**
-  **02_trainModel_roboticGripper.ipynb**
-  **03_operation_roboticGripper.ipynb**

Afinal, o projeto requer pelo menos três fases distintas:

- Captura dos gestos (rotulados) para uso futuro em aprendizagem supervisionada.
- Treinamento de um modelo utilizando rede neural de aprendizagem profunda (_deep learning_) construída com [Keras/TensorFlow](http://www.dobitaobyte.com.br/rede-neural-com-keras-mais-anotacoes/). Atenção, no site referenciado existem instruções para instalação do Keras, mas a princípio elas devem ser desconsideradas: Ao construir e utilizar o ambiente **duo_ml** a partir do arquivo **Duo_ml.yml**, todos os pacotes necessários ao projeto, inclusive Keras/Tensorflow, vão ser instalados na versão correta. O site oficial do Keras fica [aqui](https://keras.io/)
- Utilize o modelo treinado para prever comandos e operar a  garra robótica.

Bom divertimento!

©Duodécimo, December, 2017.
