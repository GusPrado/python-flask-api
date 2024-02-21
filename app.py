from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from models import Pessoas, Usuarios

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

#IMPLEMENT PASSWD HASH TO FINISH
@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()
class Pessoa(Resource):

    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.id 
            }
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'Pessoa nao encontrada'
            }
        return response
    
    def post(self, nome):
            dados = request.json
            pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
            pessoa.save()
            response = {
                'id':pessoa.id,
                'nome':pessoa.nome,
                'idade':pessoa.idade
            }
            return response

class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response
    
class Usuario(Resource):
    @auth.login_required
    def get(self,username):
            usuario = Usuarios.query.filter_by(login=username).first()
            #usuario = Usuarios.query.all()
            try:
                response = {
                    'login':usuario.login,
                    'id':usuario.id 
                }
            except AttributeError:
                print(usuario)
                response = {
                    'status':'error',
                    'mensagem':'Usuário nao encontrado'
                }
            return response
    
    def post(self, username):
            dados = request.json
            usuario = Usuarios(login=dados['login'], senha=dados['senha'])
            usuario.save()
            response = {
                'id':usuario.id,
                'login':usuario.login
            }
            return response
class Home(Resource):

    def get(self):
        return ('App funcional!!!')
    
api.add_resource(Home, '/')
api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(Usuario, '/usuario/<string:username>/')

if __name__ == '__main__':
    app.run(debug=True)
