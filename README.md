# Controle-de-validade
Algoritmo de controle de validade.

## Importante para iniciar o código:
- Deve ter o Python instalado, de preferencia em uma versão mais atualizada, caso deseja instalar: [Python](https://www.python.org/downloads/)
- Precisa instalar a biblioteca mysql.connector via cmd, para instalar use "pip install mysql-connector".
- Para iniciar o programa é necessário usar o comando "python main.py".

## Para criar a tabela MySQL:
```
CREATE DATABASE loja;
USE loja;
CREATE TABLE produtos(
    codigo VARCHAR(20),
    nome VARCHAR(20),
    marca VARCHAR(20),
    validade DATE
);
```
