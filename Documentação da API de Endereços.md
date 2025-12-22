# Documentação da API de Endereços

Este documento detalha os *endpoints* da API de gerenciamento de endereços, que utiliza o **FastAPI** e se integra ao serviço **ViaCEP** para a criação de novos registros.

## Estrutura de Dados (Schemas)

As rotas utilizam os seguintes modelos de dados (schemas) para a comunicação:

### 1. EnderecoResponse (Modelo de Resposta)

Representa a estrutura completa de um endereço armazenado no banco de dados.

| Campo | Tipo | Descrição | Exemplo |
| :--- | :--- | :--- | :--- |
| `id` | `integer` | Identificador único do endereço. | `1` |
| `cep` | `string` | Código de Endereçamento Postal. | `"01001-000"` |
| `logradouro` | `string` | Nome da rua, avenida, etc. | `"Praça da Sé"` |
| `bairro` | `string` | Nome do bairro. | `"Sé"` |
| `cidade` | `string` | Nome da cidade. | `"São Paulo"` |
| `uf` | `string` | Unidade Federativa (Estado). | `"SP"` |
| `latitude` | `string` ou `null` | Coordenada geográfica de latitude (opcional). | `"-23.5505"` |
| `longitude` | `string` ou `null` | Coordenada geográfica de longitude (opcional). | `"-46.6333"` |

### 2. EnderecoCreate (Modelo de Criação)

Utilizado para a criação de um novo endereço. **Apenas o CEP é obrigatório**, pois os demais campos são preenchidos automaticamente via consulta ao ViaCEP.

| Campo | Tipo | Descrição | Obrigatório |
| :--- | :--- | :--- | :--- |
| `cep` | `string` | Código de Endereçamento Postal a ser consultado. | Sim |

### 3. EnderecoUpdate (Modelo de Atualização)

Utilizado para a atualização de um endereço existente. Todos os campos são opcionais, permitindo a atualização parcial (comportamento de PATCH).

| Campo | Tipo | Descrição | Obrigatório |
| :--- | :--- | :--- | :--- |
| `cep` | `string` | Novo CEP. | Não |
| `logradouro` | `string` | Novo logradouro. | Não |
| `bairro` | `string` | Novo bairro. | Não |
| `cidade` | `string` | Nova cidade. | Não |
| `uf` | `string` | Nova UF. | Não |
| `latitude` | `string` ou `null` | Nova latitude. | Não |
| `longitude` | `string` ou `null` | Nova longitude. | Não |

---

## Endpoints da API

Todas as rotas estão agrupadas sob o prefixo `/enderecos`.

### 1. Criar Novo Endereço

Cria um novo registro de endereço no banco de dados, utilizando o CEP fornecido para preencher automaticamente os dados de logradouro, bairro, cidade e UF através do serviço ViaCEP.

| Detalhe | Descrição |
| :--- | :--- |
| **Método** | `POST` |
| **URL** | `/enderecos/` |
| **Tag** | `Endereços` |
| **Corpo da Requisição** | `EnderecoCreate` (JSON) |

#### Respostas

| Status Code | Descrição | Schema de Resposta |
| :--- | :--- | :--- |
| `200 OK` | Endereço criado com sucesso. | `EnderecoResponse` |
| `404 Not Found` | CEP inválido ou não encontrado pelo serviço ViaCEP. | `{"detail": "CEP inválido ou não encontrado"}` |

### 2. Obter Endereço por ID

Busca e retorna os detalhes de um endereço específico utilizando seu identificador único.

| Detalhe | Descrição |
| :--- | :--- |
| **Método** | `GET` |
| **URL** | `/enderecos/{id}` |
| **Tag** | `Endereços` |
| **Parâmetros de Caminho** | `id` (integer): O ID do endereço a ser buscado. |

#### Respostas

| Status Code | Descrição | Schema de Resposta |
| :--- | :--- | :--- |
| `200 OK` | Endereço encontrado e retornado. | `EnderecoResponse` |
| `404 Not Found` | Endereço com o ID fornecido não foi encontrado. | `{"detail": "Endereço não encontrado"}` |

### 3. Atualizar Endereço

Atualiza um ou mais campos de um endereço existente.

| Detalhe | Descrição |
| :--- | :--- |
| **Método** | `PUT` |
| **URL** | `/enderecos/{id}` |
| **Tag** | `Endereços` |
| **Parâmetros de Caminho** | `id` (integer): O ID do endereço a ser atualizado. |
| **Corpo da Requisição** | `EnderecoUpdate` (JSON) |

#### Respostas

| Status Code | Descrição | Schema de Resposta |
| :--- | :--- | :--- |
| `200 OK` | Endereço atualizado com sucesso. | `EnderecoResponse` |
| `404 Not Found` | Endereço com o ID fornecido não foi encontrado. | `{"detail": "Endereço não encontrado"}` |

### 4. Remover Endereço

Exclui um endereço do banco de dados utilizando seu identificador único.

| Detalhe | Descrição |
| :--- | :--- |
| **Método** | `DELETE` |
| **URL** | `/enderecos/{id}` |
| **Tag** | `Endereços` |
| **Parâmetros de Caminho** | `id` (integer): O ID do endereço a ser removido. |

#### Respostas

| Status Code | Descrição | Schema de Resposta |
| :--- | :--- | :--- |
| `200 OK` | Endereço removido com sucesso. | `{"mensagem": "Endereço removido com sucesso"}` |
| `404 Not Found` | Endereço com o ID fornecido não foi encontrado. | `{"detail": "Endereço não encontrado"}` |
