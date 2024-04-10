from flask import Flask
from flask_restful import Resource, Api
from models import Pessoas

# Definindo API
app = Flask(__name__)
api = Api(app)

# Criando a classe de requisição para Pessoa
class Pessoa(Resource):
    # Definindo o GET utilizando como parametro o nome
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first() # first itera o objeto(tabela)
        # Tratamento de erros para caso a pessoa não seja encontrada.
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'Pessoa não encontrada'
            }

        return response

# Definindo a rota para Pessoa  
api.add_resource(Pessoa, '/pessoa/<string:nome>/')

if __name__ == '__main__':
    app.run(debug=True)
