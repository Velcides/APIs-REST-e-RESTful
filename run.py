# Cria uma aplicação (API) mostrando a mensagem 'Hello World' no localhost na porta 5000.
from flask import Flask 

# Definindo nossa API com o Flask
app = Flask(__name__)

# Adicionando decorador para direcionar a rota padrão.
# Definindo os métodos permitidos para a API.
# variavel numero serve para pegar a URN e exibir após o Hello World. 
# ex: http://127.0.0.1:5000/100 = Hello World. 100
#@app.route("/<int:numero>", methods=['GET','POST'])
@app.route("/", methods=['GET','POST'])
# Criando função para exibir Hello World.
def hello(numero):
    return 'Hello World. {}'.format(numero)

# Chamando apenas o módulo main do Flask.
if __name__ == "__main__":
    # Rodando a aplicação e configurando para restart automático com debug=True
    # Utilizar o debug apenas no ambiente de dev.
    app.run(debug=True)