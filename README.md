<<<<<<< HEAD
# API Principal - Gerenciamento de Endereços
=======
# rotapi (API Principal) - Gerenciamento de Endereços
>>>>>>> 85ff5524929ba95deee46abea979af3b00190eac

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
<<<<<<< HEAD

## Tecnologias Utilizadas
- **Python 3.11**
- **FastAPI**
- **Uvicorn**
- **SQLite**
- **Pydantic**
- **Requests**
- **Docker**
- **Docker Compose**

=======
>>>>>>> 85ff5524929ba95deee46abea979af3b00190eac
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
<<<<<<< HEAD
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

- **API Principal**: http://localhost:8000
- **Documentação API Principal (Swagger)**: http://localhost:8000/docs
- **API Secundária**: http://localhost:8001
- **Documentação API Secundária (Swagger)**: http://localhost:8001/docs
=======

3. **Acessar as APIs:**

- **API Principal**: http://127.0.0.1:8000
- **Documentação API Principal (Swagger)**: http://127.0.0.1:8000/docs
- **API Secundária**: http://127.0.0.1:9000
- **Documentação API Secundária (Swagger)**: http://127.0.0.1:9000/docs
>>>>>>> 85ff5524929ba95deee46abea979af3b00190eac

### Opção 2: Executar com Docker (Containers Individuais)

**API Secundária:**

```bash
cd ../api-secundaria
docker build -t api-secundaria .
<<<<<<< HEAD
docker run -d -p 8001:8001 --name api-secundaria api-secundaria
=======
docker run -d -p 9000:9000 --name api-secundaria api-secundaria
>>>>>>> 85ff5524929ba95deee46abea979af3b00190eac
```

**API Principal:**

```bash
cd ../api-principal
docker build -t api-principal .
docker run -d -p 8000:8000 --name api-principal \
<<<<<<< HEAD
  -e API_SECUNDARIA_URL=http://host.docker.internal:8001 \
=======
  -e API_SECUNDARIA_URL=http://host.docker.internal:9000 \
>>>>>>> 85ff5524929ba95deee46abea979af3b00190eac
  api-principal
```

### Opção 3: Executar localmente (sem Docker)

**API Secundária:**

```bash
cd ../api-secundaria
pip install -r requirements.txt
<<<<<<< HEAD
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
=======
uvicorn app.main:app --reload --port 9000
>>>>>>> 85ff5524929ba95deee46abea979af3b00190eac
```

**API Principal (em outro terminal):**

```bash
cd ../api-principal
pip install -r requirements.txt
<<<<<<< HEAD
export API_SECUNDARIA_URL=http://localhost:8001
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Exemplos de Uso

### 1. Consultar CEP no ViaCEP

```bash
curl -X GET "http://localhost:8000/consultar-cep/01310100"
```

**Resposta:**
```json
{
  "cep": "01310-100",
  "logradouro": "Avenida Paulista",
  "complemento": "",
  "bairro": "Bela Vista",
  "localidade": "São Paulo",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "1004",
  "ddd": "11",
  "siafi": "7107"
}
```

### 2. Criar um novo endereço

```bash
curl -X POST "http://localhost:8000/enderecos" \
  -H "Content-Type: application/json" \
  -d '{
    "cep": "01310100",
    "complemento": "Próximo ao MASP",
    "latitude": -23.5613,
    "longitude": -46.6565
  }'
```

**Resposta:**
```json
{
  "id": 1,
  "cep": "01310-100",
  "logradouro": "Avenida Paulista",
  "complemento": "Próximo ao MASP",
  "bairro": "Bela Vista",
  "localidade": "São Paulo",
  "uf": "SP",
  "latitude": -23.5613,
  "longitude": -46.6565,
  "criado_em": "2024-01-15 10:30:00",
  "atualizado_em": "2024-01-15 10:30:00"
}
```

### 3. Listar todos os endereços

```bash
curl -X GET "http://localhost:8000/enderecos"
```

### 4. Buscar endereço específico

```bash
curl -X GET "http://localhost:8000/enderecos/1"
```

### 5. Atualizar endereço

```bash
curl -X PUT "http://localhost:8000/enderecos/1" \
  -H "Content-Type: application/json" \
  -d '{
    "complemento": "Em frente ao parque Trianon",
    "latitude": -23.5613,
    "longitude": -46.6565
  }'
```

### 6. Calcular distância entre dois endereços

Primeiro, crie dois endereços com coordenadas:

```bash
# Endereço 1 - São Paulo (Av. Paulista)
curl -X POST "http://localhost:8000/enderecos" \
  -H "Content-Type: application/json" \
  -d '{
    "cep": "01310100",
    "latitude": -23.5613,
    "longitude": -46.6565
  }'

# Endereço 2 - Rio de Janeiro (Copacabana)
curl -X POST "http://localhost:8000/enderecos" \
  -H "Content-Type: application/json" \
  -d '{
    "cep": "22070002",
    "latitude": -22.9711,
    "longitude": -43.1822
  }'
```

Depois, calcule a distância:

```bash
curl -X POST "http://localhost:8000/enderecos/calcular-distancia" \
  -H "Content-Type: application/json" \
  -d '{
    "endereco_origem_id": 1,
    "endereco_destino_id": 2
  }'
```

**Resposta:**
```json
{
  "distancia_km": 357.45,
  "endereco_origem": {
    "id": 1,
    "cep": "01310-100",
    "logradouro": "Avenida Paulista",
    "localidade": "São Paulo",
    "uf": "SP",
    "latitude": -23.5613,
    "longitude": -46.6565,
    ...
  },
  "endereco_destino": {
    "id": 2,
    "cep": "22070-002",
    "logradouro": "Avenida Atlântica",
    "localidade": "Rio de Janeiro",
    "uf": "RJ",
    "latitude": -22.9711,
    "longitude": -43.1822,
    ...
  }
}
```

### 7. Deletar endereço

```bash
curl -X DELETE "http://localhost:8000/enderecos/1"
```

### 8. Verificar saúde da API

```bash
curl -X GET "http://localhost:8000/health"
```

**Resposta:**
```json
{
  "status": "healthy",
  "api_secundaria": "online"
}
```

## Comandos Docker Úteis

**Parar os serviços:**
```bash
docker-compose down
```

**Ver logs:**
```bash
docker-compose logs -f
```

**Ver logs de um serviço específico:**
```bash
docker-compose logs -f api-principal
docker-compose logs -f api-secundaria
```

**Reconstruir as imagens:**
```bash
docker-compose up --build
```

**Remover volumes:**
```bash
docker-compose down -v
=======
uvicorn app.main:app --reload --port 8000
>>>>>>> 85ff5524929ba95deee46abea979af3b00190eac
```

## Banco de Dados

O projeto utiliza **SQLite** para persistência de dados. O arquivo `enderecos.db` é criado automaticamente na primeira execução.

### Estrutura da Tabela `enderecos`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária (auto-incremento) |
| cep | TEXT | CEP do endereço |
| logradouro | TEXT | Nome da rua/avenida |
<<<<<<< HEAD
| complemento | TEXT | Complemento do endereço |
| bairro | TEXT | Bairro |
| localidade | TEXT | Cidade |
| uf | TEXT | Estado (UF) |
| latitude | REAL | Coordenada de latitude |
| longitude | REAL | Coordenada de longitude |
| criado_em | TIMESTAMP | Data/hora de criação |
| atualizado_em | TIMESTAMP | Data/hora da última atualização |

## Tratamento de Erros

A API implementa tratamento de erros adequado com códigos HTTP apropriados:

- **200 OK**: Operação bem-sucedida
- **201 Created**: Recurso criado com sucesso
- **204 No Content**: Recurso deletado com sucesso
- **400 Bad Request**: Dados inválidos na requisição
- **404 Not Found**: Recurso não encontrado
- **500 Internal Server Error**: Erro interno do servidor
- **503 Service Unavailable**: Serviço externo indisponível

## Diferenciais Implementados

✅ **Código limpo e organizado**: Separação clara de responsabilidades (models, database, services)  
✅ **Validação de dados**: Uso de Pydantic para validação robusta  
✅ **Tratamento de erros**: Mensagens de erro claras e códigos HTTP apropriados  
✅ **Documentação automática**: Swagger UI e ReDoc gerados automaticamente pelo FastAPI  
✅ **Health checks**: Endpoints para monitoramento da saúde das APIs  
✅ **CORS configurado**: Permite integração com frontends  
✅ **Docker Compose**: Orquestração simplificada de múltiplos serviços  
✅ **Persistência de dados**: Banco de dados SQLite com timestamps  

## Repositórios

- **API Principal**: [Link para o repositório no GitHub]
- **API Secundária**: [Link para o repositório no GitHub]

## Autor

Desenvolvido como parte do MVP de Arquitetura de Software.

## Licença

Este projeto é de código aberto e está disponível para fins educacionais.
=======
| bairro | TEXT | Bairro |
| cidade | TEXT | Cidade |
| uf | TEXT | Estado (UF) |
| latitude | REAL | Coordenada de latitude |
| longitude | REAL | Coordenada de longitude |

## Autor

Desenvolvido por Gabriel Boniolo como parte do MVP da disciplina de Arquitetura de Software | Engenharia de Software - PUC-Rio.

## Licença

Este projeto é de código aberto e está disponível para fins educacionais.
>>>>>>> 85ff5524929ba95deee46abea979af3b00190eac
