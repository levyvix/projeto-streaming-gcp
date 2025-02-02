

# Projeto de Monitoramento de Caminhões com Sensores

## Resumo

Este projeto visa desenvolver um sistema de monitoramento de caminhões equipados com sensores, permitindo a coleta e análise de dados em tempo real. O objetivo é fornecer uma ferramenta eficiente para a gestão de frotas de caminhões, melhorando a segurança, a eficiência e a redução de custos.

## Tecnologias Utilizadas

* **Google Cloud Pub/Sub**: plataforma de mensagens em nuvem para a coleta e processamento de dados dos sensores.
* **Python**: linguagem de programação utilizada para o desenvolvimento do sistema.
* **Google Cloud**: plataforma de nuvem para armazenamento e processamento de dados.

## Motivação

A motivação para o desenvolvimento deste projeto é a necessidade de melhorar a gestão de frotas de caminhões, reduzindo custos e melhorando a segurança. Com a utilização de sensores e tecnologias de nuvem, é possível coletar e analisar dados em tempo real, permitindo a tomada de decisões mais informadas.

## Funcionalidades

* Coleta de dados dos sensores instalados nos caminhões, incluindo:
	+ Temperatura
	+ Odômetro
	+ Outros parâmetros relevantes
* Processamento e armazenamento de dados na nuvem
* Análise de dados em tempo real para detecção de anomalias e alertas
* Integração com sistemas de gestão de frotas para melhorar a eficiência e reduzir custos

## Arquitetura do Sistema

* **Coleta de Dados**: os sensores instalados nos caminhões enviam dados para o Google Cloud Pub/Sub.
* **Processamento de Dados**: os dados são processados e armazenados na nuvem utilizando o Google Cloud.
* **Análise de Dados**: os dados são analisados em tempo real para detecção de anomalias e alertas.
* **Integração com Sistemas de Gestão de Frotas**: os dados são integrados com sistemas de gestão de frotas para melhorar a eficiência e reduzir custos.


### Contribuições

Contribuições são bem-vindas! Se você tiver interesse em contribuir para o projeto, por favor, entre em contato conosco.


## Como executar o projeto

- Instale os pacotes necessários
    - google-cloud-pubsub
    - python-dotenv
- Autentique sua conta Google
    - `gcloud auth application-default login`
- Crie seu topico
- Cria seu conjunto de dados e tabela no bigquery com o esquema da sua mensagem
- Crie uma assinatura para escrever diretamente para a tabela criada, e marque a opção **Usar esquema da tabela**
- Coloque as variaveis de ambiente no arquivo **.env** usando o **example.env** como guia
- Rode o programa `send_data_pub.py` no computador onde realizou a autenticação.