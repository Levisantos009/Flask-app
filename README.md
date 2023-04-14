# Flask-app

### Este projeto é uma API Flask que implementa um endpoint /Search que retorna os 5 primeiros resultados em uma busca no google. Ele usa o Docker e o Docker Compose para facilitar a execução e o gerenciamento do ambiente de desenvolvimento.

## Requisitos
    Docker
    Docker Compose

## Como executar
## Para executar a API Flask, siga as etapas abaixo:

### 1 - Clone este repositório para sua máquina local.
### 2 - No terminal, navegue até o diretório raiz do projeto.
### 3 - Execute o seguinte comando para construir a imagem do Docker e iniciar o contêiner 
        docker-compose up:

## Acesse o seguinte URL em seu navegador para verificar se a API está funcionando corretamente: 
      http://localhost:5000/api/v1/metrics
## Acesse o seguinte URL em seu navegador para fazer a busca que desejar: 
      http://localhost:5000/api/v1/search?query={Insira_oque_deseja_buscar}
      
