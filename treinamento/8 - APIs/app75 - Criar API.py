# Nosso 1° API - FLASK E DJANGO
# FLASK $ FLASK RESTFUL

'''
1 - Definir o objetivo da API:
    ex: Iremos montar uma api de blog, onde eu poderei consultar, editar, criar e excluir postagens em um blog usando a API
    
2 - Qual será o URL base do API?
    ex: QUando você cria uma aplicação local, ele terá um url tipo https://localhost:5000 , porém quando você for subir isso para nuvem, você terá que comprar ou usar um domínio com url base, vamos imaginar um exemplo de devribas.com/api
    
3 - Quais são os endpoints?
    ex: Se seu requisito é de pode consultar, editar, criar e excluir, você terá que disponibilizar os endpoints para essas questões
        > /postagens
        
4 - Quais recurosos será disponibilizado pelo API: informações sobre as postagens

5 - Quais verbos http serão disponibilizados?
    * GET
    * POST
    * PUT
    * DELETE

6 - Quais são os URL completos para cada um?
    * GET http://localhost:5000/postagens
    * GET id http://localhost:5000/postagens/1
    * POST id http://localhost:5000/postagens/
    * PUT id http://localhost:5000/postagens/1
    * DELETE id http://localhost:5000/postagens/1
'''

from flask import Flask, jsonify, request

app = Flask(__name__)
postagens = [
    {
        'título': 'Minha Historia',
        'autor': 'Amanda Dias'
    },
    {
        'título': 'Novo Dispositivo Sony',
        'autor': 'Howard Stringer'
    },
    {
        'título': 'Lançamento do Ano',
        'autor': 'Jeff Bezos'
    }    
]

# Rota padrão - GET http://localhost:5000/
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

app.run(port=5000,host='localhost',debug=True)