# Criando API que manipula registros em uma lista dados de funcionários.
from flask import Flask, jsonify, request
import json

# Definindo nossa API com o Flask
app = Flask(__name__)

# Definindo lista que receberá os registros.
developers = [
    {'Name':'Jessica', 'Habilities':['Python', 'Flask']},
    {'Name':'Velcides', 'Habilities':['Python', 'Django']}
]

# Retorna, altera e deleta Devs.
# Definindo o retorno do usuário pelo id.
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
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
        return jsonify(developer_response)
    
    elif request.method == 'PUT':
        # Recebe os dados do put em json
        data = json.loads(request.data)
        developers[id] = data
        # Retorna o registro que foi alterado.
        return jsonify(data)
    
    elif request.method == 'DELETE':
        # Deleta o registro.
        developers.pop(id)
        # Retorna a menssagem de sucesso.
        return jsonify({'stats':'Sucess', 'message':'Deleted!'})

# Criando função para inserir devs e listar todos.
@app.route('/dev/', methods= ['POST', 'GET'])
def developers_list():
    if request.method == 'POST':
        # Recebendo dados de inserção.
        data = json.loads(request.data)
        # Inserindo dados recebidos da lista.
        developers.append(data)
        # Retorna menssagem de sucesso.
        return jsonify({'Status':'Sucess!', 'Message':'New Dev Inserted!'})
    
    elif request.method == 'GET':
        return jsonify(developers)

if __name__ == '__main__':
    app.run(debug=True)

