# 🎟️ Sistema de Gestão de Eventos

API Django REST para gerenciamento de eventos acadêmicos.

## 📋 Funcionalidades
- Cadastro de eventos, participantes e atividades
- Relacionamentos 1:N, N:N e 1:1
- Autenticação
- Dashboard completo de eventos

## 🚀 Instalação Rápida

```bash
# Clone o repositório
git clone [seu-repositorio]

# Entre na pasta
cd gestor_eventos

# Crie ambiente virtual
python -m venv venv

# Ative (Windows)
venv\Scripts\activate

# Instale dependências
pip install django djangorestframework

# Execute migrações
python manage.py migrate

# Rode o servidor
python manage.py runserver


## 🎯 Funcionalidades

### 📅 Gestão de Eventos
- Criar, ler, atualizar e excluir eventos
- Campos: nome, descrição, datas, local
- Validação de datas e campos obrigatórios

### 👥 Gestão de Participantes
- CRUD completo de participantes
- Tipos: estudante, palestrante, convidado
- Inscrição em múltiplos eventos

### 🎪 Gestão de Atividades
- Atividades por evento (palestras, workshops)
- Designação de responsável
- Controle de horários e tipos

### 🔗 Relacionamentos
- **1:N** - Evento → Atividades
- **N:N** - Evento ↔ Participantes
- **1:1** - Atividade → Responsável


## 🛠️ Tecnologias

### Backend
- **Python 3.11+** - Linguagem principal
- **Django 5.0** - Framework web
- **Django REST Framework** - API REST
- **SQLite** - Banco de dados (desenvolvimento)

### Ferramentas
- **VS Code** - Editor
- **Git** - Controle de versão
