# Banco de Dados com Robot Framework e Database Library

![Database Library](docs/thumb_readme.png)

## 👨‍💻 TECNOLOGIAS UTILIZADAS

- Python: https://www.python.org/downloads/release/python-3810/
- Docker 
    - Desktop For Windows: https://docs.docker.com/desktop/install/windows-install/
    - Desktop For Mac: https://docs.docker.com/desktop/install/mac-install/
    - Desktop For Linux: https://docs.docker.com/desktop/install/linux-install/
- Poetry: https://python-poetry.org/docs/
- Robot Framework: https://pypi.org/project/robotframework/
- Database Library: https://pypi.org/project/robotframework-appiumlibrary/2.0.0/
- VSCode: https://code.visualstudio.com/download
    - Plugin:
        - Robot Framework Language Server: https://marketplace.visualstudio.com/items?itemName=robocorp.robotframework-lsp
        - Python: https://marketplace.visualstudio.com/items?itemName=ms-python.python


## 🖥️ CONFIGURAÇÃO DO POETRY

[![POETRY](https://img.youtube.com/vi/1z4JDp-Ky9g/0.jpg)](https://www.youtube.com/watch?v=1z4JDp-Ky9g)


## 🦾 INSTALANDO DEPENDÊNCIAS DO PROJETO

``` bash
poetry install
```

## 📊 LEVANTANDO BANCO DE DADOS MYSQL VIA DOCKER COMPOSE

``` bash
docker-compose up
```

## 📊 CRIANDO BANCO DE DADOS

``` bash
python .\scripts\create_database.py
```