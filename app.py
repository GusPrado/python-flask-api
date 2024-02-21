from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas

app = Flask(__name__)
api = Api(app)

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
class Home(Resource):

    def get(self):
        return ('App funcional!!!')
    
api.add_resource(Home, '/')
api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')

if __name__ == '__main__':
    app.run(debug=True)
