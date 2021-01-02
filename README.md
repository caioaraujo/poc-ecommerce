# POC ecommerce
Prova de conceito para validar tecnologias e arquitetura.

## Requisitos
Python 3.9+ (https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/)

Recomendado:<br>
Pyenv (https://github.com/pyenv/pyenv)

## Instalação
Recomendado uso de virtual environment (venv).<br>
Ex Ubuntu: `python3.9 -m venv ~/.local/share/virtualenvs/poc-ecommerce`

Após criação, ativar a venv:<br>
Ubuntu: `source ~/.local/share/virtualenvs/poc-ecommerce/bin/activate`<br>
Para desativar basta digitar `deactivate`.

Instalar as dependências:<br>
Nota: Certifique-se de que a venv esteja ativada.<br>
`pip install -r requirements.txt`

### Criação do banco de dados
Execute: `python migrate.py migrate`

O banco de dados é salvo local no arquivo `db.sqlite3`.

### Criação do usuário admin
Execute: `python -m createsuperuser`

Preencha as informações solicitadas e utilize as credenciais no módulo admin (/admin).

## Run
Na raíz do projeto: `python manage.py runserver`
