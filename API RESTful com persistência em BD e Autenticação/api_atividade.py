from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividade, Usuarios
from flask_httpauth import HTTPBasicAuth

# Definindo autenticação
auth = HTTPBasicAuth()

# Definindo API
app = Flask(__name__)
api = Api(app)

"""
Teste Manual =====================
# Criando dicionário com usuários
USUARIOS = {
    'rafael':'123',
    'velcides':'321'
}

# Implementando a verificação de senha
@auth.verify_password
def verificacao(login, senha):
    print('validando o usuario')
    print(USUARIOS.get(login) == senha)
    if not (login, senha):
        return False
   
    return USUARIOS.get(login) == senha
"""
# Verificação de login na tabela usuarios.
@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

# Criando a classe de requisição para Pessoa
class Pessoa(Resource):
    # Definindo o GET utilizando como parametro o nome.
    @auth.login_required # Para acessar este metodo precisa estar logado.
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

    # Definindo o PUT utilizando como parametro o nome
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json

        # Definindo alteração para nome e idade.
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        
        # Commitando alterações.
        pessoa.save()

        response = {
            'id': pessoa.id, 
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }

        return response
    
    # Definindo o DELETE utilizando como parametro o nome
    def delete(self, nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        pessoa.delete()
        mensagem = 'Pessoa {} excluida com sucesso'.format(pessoa.nome)

        return {'status':'sucesso', 'mensagem':mensagem}

# Criando a classe de requisição para Listar Pessoas e inserção de pessoas
class ListarPessoas(Resource):
    # Definindo o GET de listagem
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        # For in line que traz todos os items do dicionário.
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response
    
    # Definindo o POST de inserção.
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

# Criando a classe de requisição para Listar Atividades e inserção de atividades
class ListaAtividades(Resource):
    # Definindo o GET de listagem
    def get(self):
        atividades = Atividade.query.all()
        # For in line que traz todos os items do dicionário.
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome}  for i in atividades]
        return response
    
    # Definindo o POST de inserção.
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividade(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome,
            'id':atividade.id
        }
        return response

# Definindo a rota para Pessoa  
api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListarPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)
