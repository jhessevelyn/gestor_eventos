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
