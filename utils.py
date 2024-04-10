from models import Pessoa, db_session

# Insere dados na tabela pessoa.
def insere_pessoas():
    pessoa = Pessoa(nome='Mezzomo', idade=24)
    print(pessoa)
    # Commitando esses dados.
    pessoa.save()

# Consulta dados na tabela pessoa.
def consulta_pessoas():
    pessoas = Pessoa.query.all()
    print(pessoas)
    pessoa = Pessoa.query.filter_by(nome='Velcides').first()
    print(pessoa)
    print(pessoa.idade)

# Altera dados na tabela pessoa.
def altera_pessoa():
    pessoa = Pessoa.query.filter_by(nome='Velcides').first()
    pessoa.idade = 22
    pessoa.save()

# Exclui dados na tabela pessoa.
def exclui_pessoa():
    pessoa = Pessoa.query.filter_by(nome='Mezzomo').first()
    # Commitando o delete.
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #exclui_pessoa()
    consulta_pessoas()
    #altera_pessoa()