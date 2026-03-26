#!/bin/bash

# Para executar:
# chmod +x setuphost.sh
# ./setuphost.sh


# Atualiza os pacotes
echo "Atualizando pacotes do sistema operacional ..."
sudo apt-get update

# Instala o Docker, aceitando automaticamente as confirmações
echo "Instalando Docker..."
sudo apt install -y docker.io

# Inicia o serviço do Docker
echo "Iniciando o serviço Docker..."
sudo systemctl start docker

# Habilita o Docker para iniciar automaticamente com o sistema
echo "Habilitando o Docker no boot..."
sudo systemctl enable docker

echo "Processo concluído!"
