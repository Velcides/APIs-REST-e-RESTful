# API REST que soma números.
from flask import Flask, jsonify, request
import json
# jsonify permite que a requisição retorne inforções no formato JSON.

# Definindo nossa API com o Flask
app = Flask(__name__)

@app.route("/<int:id>")
# Retorna os dados por meio de um JSON. Define o id pela route.
def person(id):
    return jsonify({'id':id, 'name':'Rafael', 'fullName':'Bastos'})

# Retorna a soma de dois valores.
'''
@app.route('/sum/<int:v1>/<int:v2>/')
def sum(v1, v2):
    return jsonify({'sum': v1 + v2})
'''
# Retornando soma pelo método POST.
@app.route('/sum', methods= ['POST', 'GET'])
def sum_v():
    # Pegando valores do postman por meio da biblioteca requests.
    # Em body>raw digite {"values" : [10, 10, 10]}
    # O json.loads converte os dados em json.
    # Request.data pega os dados do post.
    if request.method == 'POST':
        data = json.loads(request.data)
        total = sum(data['values'])
        print(data)
    elif request.method == 'GET':
        total = 10 + 10
    
    return jsonify({'sum' : total})

if __name__ == "__main__":
    app.run(debug=True)