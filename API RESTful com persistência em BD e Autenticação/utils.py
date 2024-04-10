from models import Pessoas, db_session

# Insere dados na tabela pessoa.
def insere_pessoas():
    pessoa = Pessoas(nome='Velcides', idade=24)
    print(pessoa)
    # Commitando esses dados.
    pessoa.save()

# Consulta dados na tabela pessoa.
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Velcides').first()
    print(pessoa)
    print(pessoa.idade)

# Altera dados na tabela pessoa.
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Velcides').first()
    pessoa.idade = 22
    pessoa.save()

# Exclui dados na tabela pessoa.
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Mezzomo').first()
    # Commitando o delete.
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #exclui_pessoa()
    consulta_pessoas()
    #altera_pessoa()