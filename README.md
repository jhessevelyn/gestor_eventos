# Sistema de Gestão de Eventos - API Django REST

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

> API RESTful para gestão completa de eventos, participantes e atividades. Desenvolvida como Projeto Integrador.

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivos](#objetivos)
- [Funcionalidades](#funcionalidades)
- [Arquitetura](#arquitetura)
- [Tecnologias](#tecnologias)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Execução](#execução)
- [Testes](#testes)
- [Rotas da API](#rotas-da-api)
- [Autenticação](#autenticação)
- [Modelo de Dados](#modelo-de-dados)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Diagramas](#diagramas)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Professor](#professor)

## Sobre o Projeto

O **Sistema de Gestão de Eventos** é uma API desenvolvida em Django REST Framework para gerenciar eventos acadêmicos e corporativos. A solução permite o cadastro de eventos, participantes e atividades, com relacionamentos bem definidos entre as entidades.

**Contexto:** Muitos organizadores de eventos ainda utilizam planilhas e formulários desconexos, o que gera falhas e dificuldade de gestão.

**Solução:** Centralizar todas as operações em uma API robusta e escalável.

## Objetivos

### Objetivo Geral
Desenvolver uma API Backend com autenticação para gerenciar eventos, participantes, atividades e seus relacionamentos.

### Objetivos Específicos
- Modelar entidades: Evento, Participante e Atividade
- Implementar relacionamentos: 1:N, N:N e 1:1
- Criar CRUD completo para todas as entidades
- Implementar sistema de autenticação
- Desenvolver rotas de relacionamento (mínimo 3)
- Criar rota composta A-B-C (dashboard)

## Funcionalidades

### Gestão de Eventos
- Criar, listar, atualizar e excluir eventos
- Campos: nome, descrição, data_início, data_fim, local

### Gestão de Participantes
- CRUD de participantes com tipos: estudante, palestrante, convidado
- Inscrição em múltiplos eventos (N:N)

### Gestão de Atividades
- Gerenciamento de atividades por evento
- Designação de responsável (1:1)
- Tipos: workshop, palestra, oficina

### Relacionamentos
- **1:N** - Evento → Atividade
- **N:N** - Evento ↔ Participante
- **1:1** - Atividade → Participante (responsável)

## Arquitetura
