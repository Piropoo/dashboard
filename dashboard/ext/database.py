from flask_sqlalchemy import SQLAlchemy

# Imports para criar database
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(50))
    username = db.Column(db.String(12))
    password = db.Column(db.String(16))


def init_app(app):

    db.init_app(app)


def cria_database(uri):

    engine = create_engine(uri)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()

    class Usuario(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String(100))
        email = Column(String(50))
        username = Column(String(12))
        password = Column(String(16))

    Base.metadata.create_all(engine)

    ex1 = Usuario(nome='Rogério de Souza da Silva', email='rogerio-silva@hotmail.com',
                  username='rogerin', password='senhaaleatoria')
    ex2 = Usuario(nome='Roberto de Andrade Castro', email='robertocastro@gmail.com',
                  username='robertao', password='123456')
    ex3 = Usuario(nome='Pedro Ferreira Brandão', email='pedrofb@connect.com.vc',
                  username='pedrin', password='654321')
    session.add_all([ex1, ex2, ex3])
    session.commit()


if __name__ == '__main__':

    # Pega o user
    user = input('Digite o user da sua conexão com o banco de dados mysql'
                 ' (não insira nada para deixar como "root" por padrão)\nuser:').strip()
    if user == '':
        user = 'root'

    # Pega a senha
    senha = input('Digite a senha da sua conexão com o banco de dados mysql\nsenha:')

    # Pega o host
    host = input('Digite o host da sua conexão com o banco de dados mysql'
                 ' (não insira nada para deixar como "localhost" por padrão)\nhost:').strip()
    if host == '':
        host = 'localhost'

    uri = f'mysql+mysqlconnector://{user}:{senha}@{host}/dashboard'

    cria_database(uri)

    print('Banco de dados criado com sucesso.')