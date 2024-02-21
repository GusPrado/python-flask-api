# RESTFul API com Flask

Projeto de uma API básica utilizando o framework Flask com integração com banco SQLite e autenticação de usuários.

Para instalar utilize o comando `python install -r requirements.txt`

Para rodar primeiro crie o banco, a conexão e as tabelas principais com o comando `python models.py`

Após isso para executar a aplicação principal utilize `python app.py`. O acesso deverá estar disponível em http://localhost:5000/

> Principais bibliotecas utilizadas neste projeto:
> - Flask
> - Flask-HTTPAuth
> - Flask-RESTful
> - SQLAlchemy
> - Werkzeug