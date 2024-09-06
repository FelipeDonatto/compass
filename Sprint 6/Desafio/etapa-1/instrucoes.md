### Construir a imagem com base no Dockerfile

Primeiro, você constrói a imagem utilizando o comando:

```bash
docker build -t s3_data ./
```

- O comando `docker build` cria a imagem com base no `Dockerfile` que está no diretório atual (`./`).
- A flag `-t s3_data` atribui o nome `s3_data` à imagem.

### Executar o contêiner a partir da imagem

Após construir a imagem, execute o contêiner usando o comando:

```bash
docker run s3_data
```

- O comando `docker run s3_data` cria e inicia um contêiner a partir da imagem `s3_data`.
