#!/bin/bash

# Para executar:
# chmod +x setupconainers.sh
# ./setupconainers.sh

# Valida se diretórios requeridos existem
[ ! -d "$(pwd)/models" ] && echo "Diretório 'models' não encontrado!" && exit 1
[ ! -d "$(pwd)/config" ] && echo "Diretório 'config' não encontrado!" && exit 1
[ ! -d "$(pwd)/Log" ]    && echo "Diretório 'Log' não encontrado!" && exit 1


# Função para verificar, parar e remover um container
handle_existing_container() {
  local container_name=$1
  if [ "$(sudo docker ps -aq -f name=$container_name)" ]; then
    echo "Parando e removendo o container '$container_name'..."
    sudo docker stop $container_name
    sudo docker rm $container_name
  fi
}

# Maneja containers existentes
handle_existing_container "serving01"
handle_existing_container "serving02"
handle_existing_container "modelmanager"

# Criação da rede Docker
echo "Criando a rede Docker..."
sudo docker network create plat_network || echo "Rede 'plat_network' já existe."

# Inicialização do container serving01
echo "Iniciando o container 'serving01'..."
sudo docker run -d --network plat_network --restart always -v $(pwd)/models:/myServer/models --name serving01 platserver python servingmodel.py models/modelo01.joblib

# Inicialização do container serving02
echo "Iniciando o container 'serving02'..."
sudo docker run -d --network plat_network --restart always -v $(pwd)/models:/myServer/models --name serving02 platserver python servingmodel.py models/modelo02.joblib

# Inicialização do container modelmanager
echo "Iniciando o container 'modelmanager'..."
sudo docker run -d --network plat_network -p 443:8080 --restart always -v $(pwd)/config:/myServer/config -v $(pwd)/Log:/myServer/Log --name modelmanager platserver python modelmanager.py

# Esperar 5 segundos antes de listar os containers
echo "Aguardando 5 segundos para verificar os containers..."
sleep 5

# Listar os containers em execução
echo "Listando os containers que estão em execução:"
sudo docker ps -a