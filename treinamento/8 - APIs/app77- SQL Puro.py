# SQL - Structured Query Language
# db.sqlite3
import sqlite3

with sqlite3.connect('artistas.db') as conexao:
    # Criar uma conexao com o banco de dados
    sql = conexao.cursor()
    # Rodar Comando SQL
    sql.execute('create table banda(nome text, estilo text, membros interger);')
    # Exemplo de inserir dados
    sql.execute('insert into banda(nome, estilo, membros) values ("Banda 1", "Rock", 3)')
    
    # Exemplo de usar dados da minha aplicação em um comando SQL
    nome = input('Digite o nome da banda ')
    estilo = input('Digite o estilo da banda ')
    quantidade_integrantes = int(input('Quantidade de integrantes da banda '))
    
    sql.execute('insert into banda values(?,?,?)',[nome,estilo,quantidade_integrantes])
    # Salvando alterações no bando de dados
    conexao.commit()
    
    # Exibir dados no console python(terminal)
    bandas = sql.execute('select * from banda;')
    for banda in bandas:
        print(banda)