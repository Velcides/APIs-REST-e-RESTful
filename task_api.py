# Criando API que gerencia cadastro de tarefas.
from flask import Flask, jsonify, request
import json

# Definindo nossa API com o Flask
app = Flask(__name__)

# Definindo lista que receberá as tarefas.
tasks = [
    {
        'id': 0,
        'Responsible':'Jessica',
        'Task':'Desenvolver o método GET',
        'Stats':'Concluido'
    },
    {
        'id': 1,
        'Responsible':'Velcides',
        'Task':'Desenvolver o método PUT',
        'Stats':'Concluido'
    }
]

# Retorna, altera e deleta Tasks.
# Definindo o retorno da task pelo id.
@app.route('/task/<int:id>/', methods=['GET', 'DELETE'])
def developer(id):
    if request.method == 'GET':
       # Tratamento de erros para o caso da task for deletada/"desindexada"
        try:
            # Relacionando o id da lista ao id da task.
            task_response = tasks[id]
            print(task_response)
        except IndexError:
            message = 'Task in ID {} doesn´t exist'.format(id)
            task_response = {'status':'Error', 'Message':message}
        except Exception:
            message = 'Unknown Exception!'
            task_response = {'status':'Error', 'Message':message}

        # Retorna o registro.
        return jsonify(task_response)
    
    elif request.method == 'DELETE':
        # Deleta o registro.
        tasks.pop(id)
        # Retorna a menssagem de sucesso.
        return jsonify({'stats':'Sucess', 'message':'Deleted!'})

# Criando função para inserir task e listar todas.
@app.route('/task/', methods= ['POST', 'GET'])
def tasks_list():
    if request.method == 'POST':
        # Recebendo dados de inserção.
        data = json.loads(request.data)
        # Inserindo dados recebidos da lista.
        tasks.append(data)
        # Retorna menssagem de sucesso.
        return jsonify({'Status':'Sucess!', 'Message':'New Dev Inserted!'})
    
    elif request.method == 'GET':
        return jsonify(tasks)
    
# Rota para alterar o campo Stats de uma tarefa com o método PUT
@app.route('/task/<int:id>/<stats>', methods=['PUT'])
def change_stats(id, stats):
    # Itera sobre as tarefas
    for task in tasks:
        # Verifica se a tarefa atual tem o mesmo ID fornecido na URL
        if task['id'] == id:
            # Atualiza o campo Stats da tarefa
            task['Stats'] = stats
            # Retorna a tarefa atualizada em formato JSON com código de status 200 (OK)
            return jsonify(task), 200
    # Se a tarefa com o ID fornecido não for encontrada, retorna um JSON indicando o erro com código de status 404 (Not Found)
    return jsonify({'error': 'Tarefa não encontrada'}), 404
    
if __name__ == '__main__':
    app.run(debug=True)

