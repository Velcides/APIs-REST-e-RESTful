# Criando API RESTful que manipula registros em uma lista dados de funcionários.
from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilities import Habilities, HabilitiesModifier

# Definindo nossa API com o Flask
app = Flask(__name__)
# Definindo nossa API com o Flask-RESTful
api = Api(app)

# Definindo lista que receberá os registros.
developers = [
    {'id': 0, 'Name':'Jessica', 'Habilities':['Python', 'Flask']},
    {'id': 1,'Name':'Velcides', 'Habilities':['Python', 'Django']}
]

# Criando Classe com funções para Retornar, alterar e deletar Devs.
class Developers(Resource):
    def get(self, id):
        # Tratamento de erros para o caso do usuário for deletado/"desindexado"
        try:
            # Relacionando o id da lista ao id do dev.
            developer_response = developers[id]
            print(developer_response)
        except IndexError:
            message = 'Developer in ID {} doesn´t exist'.format(id)
            developer_response = {'status':'Error', 'Message':message}
        except Exception:
            message = 'Unknown Exception!'
            developer_response = {'status':'Error', 'Message':message}

        # Retorna o registro.
        return developer_response
    
    def put(self, id):
        # Recebe os dados do put em json
        data = json.loads(request.data)
        developers[id] = data
        # Retorna o registro que foi alterado.
        return data

    def delete(self, id):
        # Deleta o registro.
        developers.pop(id)
        # Retorna a menssagem de sucesso.
        return {'stats':'Sucess', 'message':'Deleted!'}

# Criando Classe com funções para inserir devs e listar todos.   
class DevelopersList(Resource):
    def post(self):
        # Recebendo dados de inserção.
        data = json.loads(request.data)
        # Atribuindo o número do id por meio da posição no dict.
        position = len(developers)
        data['id'] = position
        # Inserindo dados recebidos da lista.
        developers.append(data)
        # Retorna menssagem de sucesso.
        return {'Status':'Sucess!', 'Message':'New Dev Inserted!'}

    def get(self):
        return developers

# Definindo as routes.
api.add_resource(Developers, '/dev/<int:id>/')
api.add_resource(DevelopersList, '/dev/')
api.add_resource(Habilities, '/habilities/')
api.add_resource(HabilitiesModifier, '/habilities/<int:id>/')



if __name__ == '__main__':
    app.run(debug=True)