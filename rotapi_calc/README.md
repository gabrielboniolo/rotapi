<<<<<<< HEAD
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
=======
# rotapi_calc (API Secundária) - Cálculo de Distâncias

## Descrição

API REST desenvolvida em Python com FastAPI para calcular distâncias entre coordenadas geográficas utilizando a fórmula de Haversine. Esta API faz parte de um sistema modular de gerenciamento de endereços.

## Funcionalidades

- **Cálculo de distância**: Calcula a distância em quilômetros entre dois pontos geográficos
- **Validação de coordenadas**: Valida e fornece informações sobre coordenadas geográficas
- **Health check**: Endpoint para verificar o status da API

## Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI**: Framework web moderno e rápido
- **Uvicorn**: Servidor ASGI de alta performance
- **Pydantic**: Validação de dados
- **Docker**: Containerização da aplicação

## Instalação e Execução

### Pré-requisitos

- Python 3.11 ou superior
- Docker (opcional, mas recomendado)

### Opção 1: Executar com Docker (Recomendado)

1. **Construir a imagem Docker:**

```bash
docker build -t api-secundaria .
```

2. **Executar o container:**

```bash
docker run -d -p 8001:8001 --name api-secundaria api-secundaria
```

3. **Acessar a API:**

- API: http://localhost:9000
- Documentação interativa (Swagger): http://localhost:9000/docs

### Opção 2: Executar localmente

1. **Instalar dependências:**

```bash
pip install -r requirements.txt
```

2. **Executar a aplicação:**

```bash
uvicorn app.main:app --reload --port 9000
```

3. **Acessar a API:**

- API: http://localhost:9000
- Documentação interativa: http://localhost:9000/docs

## Fórmula de Haversine

A fórmula de Haversine é utilizada para calcular a distância entre dois pontos na superfície de uma esfera (Terra) dados suas latitudes e longitudes. É uma fórmula importante em navegação e sistemas de geolocalização.

## Autor

Desenvolvido por Gabriel Boniolo como parte do MVP da disciplina de Arquitetura de Software | Engenharia de Software - PUC-Rio.

## Licença

Este projeto é de código aberto e está disponível para fins educacionais.
>>>>>>> refs/remotes/origin/main
