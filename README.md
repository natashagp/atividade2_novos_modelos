# Conteúdo MLOPS

Atualização do Material de MLOps para o ano 2025.

Python version: 3.10.

# Preparação do ambiente

Este projeto foi preparado para ser executado em Python 3.10.

O ambiente pode ser criado com o gerenciador de sua preferência. 

## Via conda environment manager
Após ter o conda instalado, execute:
```shell
conda env create -f environment.yml
```
Para verificar os ambientes criados e disponíveis:
```commandline
conda env list
```

Documentação de referência: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html 

## Via outros gerenciadores de ambiente
Após ter a versão do Python devidamente instalada, execute:
```shell
pip install -r requirements.txt
```

## Dependências Azure Machine Learning
Se o você for integrar cin a área de trabalho Azure Macbine Learning, instale também as dependências da Azure:
```shell
pip install -r requirements_azure.txt
```

# Estrutura de Arquivos e Pastas

Este projeto contém os seguintes arquivos e pastas, cada um com uma funcionalidade específica:

---

## **Pastas**

### `Log/`
- Diretório para armazenar os logs gerados durante a execução dos scripts ou containers. 
- Útil para depuração e monitoramento de erros.

### `azurefunctions/`
- Contém implementações relacionadas a funções no Microsoft Azure.
- Inclui código para integração de funcionalidades serverless na nuvem.

### `config/`
- Contém arquivos de configuração usados para personalizar o comportamento dos scripts e serviços.
- Exemplos: Configurações de rede, parâmetros de execução, etc.

### `datasets/`
- Diretório para armazenar datasets usados para treinar e avaliar os modelos.
- Ideal para organizar arquivos de entrada do pipeline de machine learning.

### `dockerbuilds/`
- Contém arquivos necessários para construir imagens Docker personalizadas.
- Inclui scripts e Dockerfiles usados no processo de deploy.

### `models/`
- Diretório para armazenar modelos de machine learning treinados.
- Exemplos: Arquivos `.joblib`, `.pkl`, ou outros formatos.

---

## **Arquivos**

### `README.md`
- Este arquivo, que contém a documentação do projeto.

### `environment.yml`
- Arquivo de configuração para gerenciar dependências no Conda.
- Permite recriar o ambiente de execução.

### `geraconfig.sh` 
- Script para gerar arquivos de configuração automaticamente.
- Facilita o processo de configuração inicial, quando necessário recriar alguma configuração.

### `modelmanager.py`
- Script principal para execução em contêiner de gerenciamento de modelos.

### `requirements.txt`
- Lista de dependências do projeto para instalação via `pip`.
- Deve ser usado para configurar o ambiente Python.

### `requirements_azure.txt`
- Dependências específicas para execução no ambiente Azure.
- Contém pacotes necessários para integração com serviços da nuvem.

### `servingmodel.py`
- Script principal para execução em contêiner de inferência de modelos.
- Normalmente, os projetos possuem scripts de execução específicos, mas neste caso o serving está simplificado em um único script.


### `train_model.py`
- Script para treinar modelos de machine learning.
- Como o repositório já possui modelos, este script é usado apenas para recalibragem dos coeficientes.
- Inclui passos como pré-processamento, treinamento e salvamento/exportação do modelo.