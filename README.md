# API Secundária – Cálculo de Distância

## Descrição

API REST desenvolvida em Python com FastAPI para gerenciamento de endereços. A aplicação integra-se com a **API ViaCEP** (serviço externo) para buscar dados de endereços e com uma **API secundária** para calcular distâncias entre coordenadas geográficas. Os dados são persistidos em um banco de dados SQLite.

## Objetivo

Este projeto faz parte de um MVP de arquitetura de software modular, demonstrando a comunicação entre múltiplos serviços seguindo o padrão REST.

## Arquitetura do Sistema

```
┌─────────────────┐
│   API Principal │
│   (FastAPI)     │
└────────┬────────┘
         │
         ├─────────────────┐
         │                 │
         ▼                 ▼
┌─────────────────┐  ┌──────────────────┐
│   API ViaCEP    │  │  API Secundária  │
│   (Externa)     │  │   (FastAPI)      │
│   Consulta CEP  │  │                  │
└─────────────────┘  └──────────────────┘
         │                 │
         │                 │
         ▼                 ▼
    Dados de          Cálculo de
    Endereços         Distâncias
```

## Tecnologias Utilizadas
- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic

## Funcionalidades

### API Principal
- **POST /enderecos**: Cria um novo endereço consultando o ViaCEP
- **GET /enderecos**: Lista todos os endereços cadastrados
- **GET /enderecos/{id}**: Busca um endereço específico
- **PUT /enderecos/{id}**: Atualiza um endereço existente
- **DELETE /enderecos/{id}**: Remove um endereço
- **POST /enderecos/calcular-distancia**: Calcula distância entre dois endereços usando a API secundária
- **GET /consultar-cep/{cep}**: Consulta CEP no ViaCEP sem salvar
- **GET /health**: Verifica status da API e dependências

### API Secundária
- **POST /calcular-distancia**: Calcula distância entre coordenadas
- **POST /validar-coordenadas**: Valida coordenadas geográficas
- **GET /health**: Verifica status da API

### API Externa - ViaCEP
- **Serviço**: [ViaCEP](https://viacep.com.br/)
- **Licença**: Gratuito e de uso público
- **Cadastro**: Não é necessário
- **Rota utilizada**: `GET https://viacep.com.br/ws/{cep}/json/`
- **Funcionalidade**: Consulta de endereços brasileiros por CEP

## Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI**
- **Uvicorn**
- **SQLite**
- **Pydantic**
- **Requests**
- **Docker**
- **Docker Compose**

## Estrutura do Projeto

```
api-principal/
├── app/
│   ├── __init__.py         # Inicialização do pacote
│   ├── main.py             # Aplicação principal e rotas
│   ├── models.py           # Modelos de dados (Pydantic)
│   ├── database.py         # Configuração e operações do banco
│   └── services.py         # Serviços externos (ViaCEP e API Secundária)
├── Dockerfile              # Instruções para criar imagem Docker
├── docker-compose.yml      # Orquestração dos serviços
├── requirements.txt        # Dependências Python
└── README.md              # Documentação
```
