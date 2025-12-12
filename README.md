
# 🐱‍🏍 Sistema de Gestão de Eventos - API Django REST

### Orientador
**Henrique Pereira de Freitas Filho** (Contato: henrique.filho@ifb.edu.br)

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![DRF](https://img.shields.io/badge/DRF-3.15-red)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📚 Índice

* [1. Sobre o Projeto](#1-sobre-o-projeto)
* [2. Objetivos](#2-objetivos)
* [3. Tecnologias & Arquitetura](#3-tecnologias--arquitetura)
* [4. Funcionalidades Detalhadas](#4-funcionalidades-detalhadas)
* [5. Configuração do Ambiente](#5-configuração-do-ambiente)
* [6. Rotas Principais da API](#6-rotas-principais-da-api)
* [7. Estrutura e Modelos](#7-estrutura-e-modelos)
* [8. Implementação (Deploy)](#8-implementação-deploy)
* [9. Contribuição & Licença](#9-contribuição--licença)

## 1. Sobre o Projeto

O **Sistema de Gestão de Eventos** é uma API desenvolvida em Django REST Framework para gerenciamento de eventos acadêmicos e corporativos. A solução permite o cadastro de eventos, participantes e atividades, com relacionamentos bem definidos entre as entidades.

**Contexto:** Muitos organizadores de eventos ainda utilizam planilhas e formulários desconexos, o que gera falhas e dificuldade de gestão.

**Solução:** Centralizar todas as operações em uma API robusta e escalável.


## 2. Objetivos

### Objetivo Geral
Desenvolver uma API Backend com autenticação segura para gerenciar eventos, participantes, atividades e seus relacionamentos. 

### Objetivos Específicos
* Modelagem de Entidades: **Evento**, **Participante** e **Atividade**.
* Implementação de Relacionamentos: 1:N, N:N e 1:1.
* Criação de CRUD (Create, Read, Update, Delete) completo para todas as entidades.
* Implementação de sistema de **autenticação JWT**
* Desenvolvimento de **rotas de relacionamento** 
* Criação de **rota composta A-B-C**


## 3. Tecnologias & Arquitetura

### 💻 Tecnologias (Exódos Utilizados)
| Categoria | Tecnologia | Versão | Propósito |
| :--- | :--- | :--- | :--- |
| **Backend** | Python | 3.11+ | Linguagem principal |
| **Web Framework** | Django | 5.0 | Estrutura web principal |
| **API** | Django REST Framework | 3.15 | Toolkit para construção de APIs REST |
| **Autenticação** | Simple JWT | 5.3 | Gerenciamento de tokens de acesso |
| **Ferramentas** | Git, VS Code | - | Controle de versão e Ambiente de Desenvolvimento |

### 🏛️ Arquitetura
A arquitetura é organizada em camadas :

* Camada de API: Endpoints REST 
* Camada de negócios: Visualizações e serializadores
* Camada de Dados: Modelos Django 
* Camada de autenticação: Autenticação JWT).

## 4. Funcionalidades Detalhadas

| Entidade | Funcionalidade Principal | Relacionamento |
| :--- | :--- | :--- |
| **Eventos** | CRUD completo; Campos: `nome`, `descrição`, `data_início`, `data_fim`, `local`. | **1:N** com Atividade |
| **Participantes** | CRUD; Tipos: `estudante`, `palestrante`, `convidado`. | **N:N** com Evento |
| **Atividades** | Gerenciamento de atividades por evento; Tipos: `workshop`, `palestra`, `oficina`. | **1:N** com Participante (Responsável) |


## 5. Configuração do Ambiente

### 🔑 Pré-requisitos
Certifique-se de ter instalado:
* Python 3.11 ou superior
* Pip (gerenciador de pacotes)

### 6. 💾 Modelo de Dados (Diagramas)

📂Diagrama Entidade-Relacionamento (DER)
![Image alt](https://github.com/jhessevelyn/gestor_eventos/blob/52a0ff0605043da8c6e9a770a64d732621a26611/IMG-20251212-WA0028.jpg)

📂Diagrama Entidade-Relacionamento (ER)
![Image alt](https://github.com/jhessevelyn/gestor_eventos/blob/e4afbe67a21721ebf6ee495677b1e845427f201c/IMG-20251204-WA0044(1).jpg)


**Verificação Rápida:**
```bash
python --version
pip --version
```

🛠️ Instalação e Execução
Siga os passos abaixo para configurar o ambiente local:
1. Clone o repositório:
```
git clone [https://github.com/usuario/projeto_api.git](https://github.com/usuario/projeto_api.git)
cd projeto_api
```

2. Crie e Ative um Ambiente Virtual:
```
python -m venv venv
```
```
# Linux/Mac
source venv/bin/activate  
```
```
# Windows
venv\Scripts\activate     
```
3. Instale as Dependências:
```
pip install -r requirements.txt
````
4. Configure as Variáveis de Ambiente:
```
cp .env.example .env
```
6. Aplique as Migrações e Inicie o Servidor:
```
python manage.py migrate
```
```
python manage.py runserver
```

O servidor estará acessível em ```http://127.0.0.1:8000/```

6. Rotas Principais da API

| Método | Endpoint (Exemplo) | Descrição | Autenticação |
|---|---|---|---|
| GET | /api/eventos/ | Lista todos os eventos | Opcional/Requerida  |
| POST | /api/participantes/ | Cria um novo participante | Requerida |
| GET | /api/eventos/{id}/ | Recupera um evento específico | Opcional |
| POST | /api/auth/token/ | Obter Token JWT | Não Aplicável |
| GET | /api/dashboard/ | Rota Composta A-B-C (Visão Gerencial) | Requerida |

7. Estrutura e Modelos
📂 Estrutura do Projeto
eventos/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── serializers.py 
├── tests.py
├── views.py
├── gestor_eventos/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py


8. Implementação (Deploy)

FALTA🛑

9. Contribuição & Licença
🤝 Contribuição

FALTA 🛑

📜 Licença

FALTA 🛑

👨‍🏫 Professor/Orientador
Henrique Pereira de Freitas Filho (henrique.filho@ifb.edu.br)

