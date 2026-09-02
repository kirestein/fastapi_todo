# FastAPI Todo

Projeto pessoal para demonstrar minhas habilidades com desenvolvimento de APIs em Python usando FastAPI, organização com Poetry e boas práticas de qualidade de código com Ruff e automação de tarefas com Taskipy.

## Visão geral

Este projeto tem como objetivo criar uma API REST para gerenciamento de tarefas, com foco em:

- estrutura limpa e escalável;
- uso de FastAPI para criação de endpoints modernos;
- gerenciamento de dependências com Poetry;
- qualidade e padronização de código com Ruff;
- automação de tarefas com Taskipy;
- testes e cobertura de código com Pytest e pytest-cov.

## Stack

- Python 3.13
- FastAPI
- Poetry
- Ruff
- Taskipy
- Pytest

## Requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.13+
- Poetry

## Instalação

Clone o projeto:

```bash
git clone <url-do-repositorio>
cd fastapi_todo
```

Crie e ative o ambiente virtual com Poetry:

```bash
poetry install
poetry shell
```

Se quiser instalar uma nova dependência do projeto:

```bash
poetry add fastapi[standard]
```

Para adicionar dependências de desenvolvimento:

```bash
poetry add --group dev ruff
poetry add --group dev pytest
poetry add --group dev pytest-cov
poetry add --group dev taskipy
```

Se quiser instalar um pacote específico em um grupo já existente:

```bash
poetry add --group dev black
poetry add --group dev mypy
```

Para remover uma dependência:

```bash
poetry remove package-name
```

Para verificar o ambiente atual:

```bash
poetry env info
poetry show
```

## Comandos úteis

Este projeto usa Taskipy para executar tarefas de desenvolvimento. Os comandos configurados estão disponíveis através do Poetry:

```bash
poetry run task lint
poetry run task format
poetry run task test
poetry run task run
```

### Descrição das tarefas

- `poetry run task lint`: executa a checagem de código com Ruff.
- `poetry run task format`: formata o código com Ruff.
- `poetry run task test`: executa os testes com Pytest e gera cobertura.
- `poetry run task run`: inicia a aplicação FastAPI em modo de desenvolvimento.

## Execução da aplicação

Para iniciar a API localmente:

```bash
poetry run task run
```

A aplicação será iniciada em modo de desenvolvimento com recarga automática.

## Qualidade de código

O projeto utiliza o Ruff como ferramenta de lint e formatação, garantindo padrões consistentes e código mais limpo.

Exemplo de comandos:

```bash
poetry run ruff check .
poetry run ruff check --fix .
poetry run ruff format .
```

## Testes

Os testes são executados com Pytest e também há integração com cobertura de código via pytest-cov.

```bash
poetry run pytest
poetry run pytest --cov=fastapi_todo --cov-report=html
```

## Estrutura do projeto

```text
fastapi_todo/
    __init__.py
    app.py

tests/
    __init__.py
pyproject.toml
README.md
requirements.txt
```

## Observações

Este projeto foi pensado como um portfólio técnico para demonstrar domínio em:

- APIs REST com FastAPI;
- organização de projetos Python;
- uso de gerenciador de dependências moderno;
- boas práticas com lint e formatação;
- automação de tarefas no fluxo de desenvolvimento.

## Autor

Erik Proença

## Licença

Este projeto é para fins de demonstração e estudo.
