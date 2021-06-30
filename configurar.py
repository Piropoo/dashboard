from dashboard.ext.database import cria_database

# Pega o user
print('Aviso: Antes de configurar é necessário criar uma database vazia no seu mysql com o nome "dashboard" '
      'caso não exista."')
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

try:
    # Cria o arquivo settings.toml
    arquivo = open('settings.toml', 'w')
    arquivo.write(f"""
[default]
SQLALCHEMY_DATABASE_URI= '{uri}'
    
SECRET_KEY = '7d0faf'
    
EXTENSIONS = [
    'dashboard.ext.database',
    
    'dashboard.blueprints.views'
]
""")

    print('Arquivo settings.toml criado com sucesso.')

    # Pergunta se quer criar database
    criar_database = ''
    while not (criar_database == 's' or criar_database == 'n'):
        criar_database = input('Deseja criar as tabelas no banco de dados? '
                               '(Para isso você precisa ter um database/schema) criado no mysql com o nome "dashboard"'
                               '\n(s) or (n):').strip().lower()
        if not (criar_database == 's' or criar_database == 'n'):
            continue

    if criar_database == 's':
        cria_database(uri)
        print('Database criada com sucesso.')

    print('App configurado com sucesso. Caso queira criar as tabelas, execute o arquivo '
          'database.py dentro do diretório: dashboard/ext/')

except:
    'Ocorreu um erro durante a configuração.'
