# Sistema de Aferição de Presença com Reconhecimento Facial

Este projeto consiste em um sistema Python que utiliza reconhecimento facial para aferir a presença de alunos em uma sala de aula e envia os dados para o AdafruitIO.

## Descrição

O sistema é capaz de capturar imagens por meio de uma câmera, identificar rostos dos alunos presentes na sala de aula e registrar sua presença por meio da integração com o AdafruitIO, um serviço de nuvem para IoT.

## Funcionamento

O sistema utiliza a biblioteca OpenCV em Python para realizar a detecção e reconhecimento facial. Se identificado, envia um registro de presença para o AdafruitIO.

<img src="https://github.com/mariamandafm/PresencaAula/assets/67834977/1055257b-3b96-41ea-bb46-a123d5be1a06" width="500" >

## Pré-requisitos

- Python 3.x
- OpenCV
- Adafruit_IO Python Library

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu_usuario/nome_do_repositorio.git
    cd nome_do_repositorio
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

- Certifique-se de configurar as credenciais do AdafruitIO.
- Execute o programa:

    ```bash
    python presenca.py
    ```

