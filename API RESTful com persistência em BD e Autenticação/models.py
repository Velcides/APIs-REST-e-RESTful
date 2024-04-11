# Código onde ficarão os módelos de classes a serem persistidas no banco de dados.
# Importando os módulos necessários do SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Criando uma instância SQLite (instância de Banco de dados).
# Aqui estamos criando um mecanismo de banco de dados SQLite chamado atividades.db no diretório atual.
engine = create_engine('sqlite:///atividades.db')

# Criando sessão para acessar o Banco de dados.
# A função scoped_session cria uma sessão de banco de dados com suporte a escopo.
# A função sessionmaker cria uma fábrica de sessões que por sua vez é encapsulada por scoped_session.
# Isso garante que uma única sessão seja usada em todo o aplicativo.
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

# Declarando uma classe base para os modelos de classes que serão persistidos no banco de dados.
# Esta classe base contém funcionalidades comuns para todos os modelos de classes.
Base = declarative_base()

# Configurando a propriedade de consulta da classe base.
# Base.query permite fazer consultas ao banco de dados usando a sessão criada anteriormente.
Base.query = db_session.query_property()

# Criando as classes (Tabelas).
class Pessoas(Base):
    __tablename__='pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)
    
    # Def para inserir uma Pessoa.
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Def para deletar uma Pessoa.
    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividade(Base):
    __tablename__='atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")
    
     # Def para inserir uma Atividade.
    def save(self):
        db_session.add(self)
        db_session.commit()

    def __repr__(self):
        return '<Atividade {}>'.format(self.nome)
    
class Usuarios(Base):
    __tablename__='usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))

    def __repr__(self):
        return '<Usuario {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

# Função que cria o banco de dados.
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()