# rotapi (API Principal) - Gerenciamento de Endereços

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
## Funcionalidades

### rotapi (API Principal)
- **POST /enderecos**: Cria um novo endereço consultando o ViaCEP
- **GET /enderecos**: Lista todos os endereços cadastrados
- **GET /enderecos/{id}**: Busca um endereço específico
- **PUT /enderecos/{id}**: Atualiza um endereço existente
- **DELETE /enderecos/{id}**: Remove um endereço
- **POST /enderecos/calcular-distancia**: Calcula distância entre dois endereços usando a API secundária
- **GET /consultar-cep/{cep}**: Consulta CEP no ViaCEP sem salvar
- **GET /health**: Verifica status da API e dependências

### rotapi_calc (API Secundária)
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

## Instalação e Execução

### Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.11 ou superior (para execução local)

### Opção 1: Executar com Docker Compose (Recomendado)

Esta opção executa automaticamente a API Principal e a API Secundária.

1. **Clone ou navegue até o diretório do projeto:**

```bash
cd api-principal
```

2. **Execute o Docker Compose:**

```bash
docker-compose up --build
```

3. **Acessar as APIs:**

- **API Principal**: http://127.0.0.1:8000
- **Documentação API Principal (Swagger)**: http://127.0.0.1:8000/docs
- **API Secundária**: http://127.0.0.1:9000
- **Documentação API Secundária (Swagger)**: http://127.0.0.1:9000/docs

### Opção 2: Executar com Docker (Containers Individuais)

**API Secundária:**

```bash
cd ../api-secundaria
docker build -t api-secundaria .
docker run -d -p 9000:9000 --name api-secundaria api-secundaria
```

**API Principal:**

```bash
cd ../api-principal
docker build -t api-principal .
docker run -d -p 8000:8000 --name api-principal \
  -e API_SECUNDARIA_URL=http://host.docker.internal:9000 \
  api-principal
```

### Opção 3: Executar localmente (sem Docker)

**API Secundária:**

```bash
cd ../api-secundaria
pip install -r requirements.txt
uvicorn app.main:app --reload --port 9000
```

**API Principal (em outro terminal):**

```bash
cd ../api-principal
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Banco de Dados

O projeto utiliza **SQLite** para persistência de dados. O arquivo `enderecos.db` é criado automaticamente na primeira execução.

### Estrutura da Tabela `enderecos`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária (auto-incremento) |
| cep | TEXT | CEP do endereço |
| logradouro | TEXT | Nome da rua/avenida |
| bairro | TEXT | Bairro |
| cidade | TEXT | Cidade |
| uf | TEXT | Estado (UF) |
| latitude | REAL | Coordenada de latitude |
| longitude | REAL | Coordenada de longitude |

## Autor

Desenvolvido por Gabriel Boniolo como parte do MVP da disciplina de Arquitetura de Software | Engenharia de Software - PUC-Rio.

## Licença

Este projeto é de código aberto e está disponível para fins educacionais.
