# POC ecommerce
Prova de conceito para validar tecnologias e arquitetura.

## Requisitos
Python 3.10+

Recomendado:<br>
Pyenv (https://github.com/pyenv/pyenv)

## Instalação
Recomendado uso de virtual environment (venv).<br>
Ex Ubuntu: `python3.10 -m venv ~/.local/share/virtualenvs/poc-ecommerce`

Após criação, ativar a venv:<br>
Ubuntu: `source ~/.local/share/virtualenvs/poc-ecommerce/bin/activate`<br>
Para desativar basta digitar `deactivate`.

Instalar as dependências:<br>
Nota: Certifique-se de que a venv esteja ativada.<br>
`pip install -r requirements.txt`

### Criação do banco de dados
Execute: `python manage.py migrate`

O banco de dados é salvo local no arquivo `db.sqlite3`.

### Criação do usuário admin
Execute: `python manage.py createsuperuser`

Preencha as informações solicitadas e utilize as credenciais no módulo admin (/admin).

## Run
Na raíz do projeto: `python manage.py runserver`

## Testes
Pré-requisito: Instalar as dependências de desenvolvimento (requirements-dev.txt).<br>
Executar todos os testes: `python manage.py test`

## Formatação do código
Para formatar o código, instale as dependências de desenvolvimento (requirements-dev.txt) e execute na raíz 
do projeto:<br>
`black .`
