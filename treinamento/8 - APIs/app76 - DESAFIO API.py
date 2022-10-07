""" DESAFIO API músicas 🥇

### 1. Definir o objetivo da API:

Iremos montar uma api de mússicas, onde deverá ser possível, consultar todas canções disponíveis, consultar uma canção individual, editar canções existentes e também excluir músicas existentes.

### 2. Qual será o URL base da API?

Iremos utilizar o url base 'localhost'

### 3. Quais são os endpoints?

Disponibilize endpoints para consultar, editar, criar e excluir

### 4. Quais recursos serão disponibilizados pela API?

Informações sobre canções

### 5. Quais verbos http serão disponibilizados?

* GET

* POST

* PUT

* DELETE

### 6. Quais são os URLs completos para cada um?

* GET http://localhost:5000/cancoes

* GET http://localhost:5000/cancoes/1

* POST http://localhost:5000/cancoes

* PUT http://localhost:5000/cancoes/1

* DELETE http://localhost:5000/cancoes/1

### 7. Qual deve ser a estrutura de cada canção

 - lista de dicionários, que contem cancao e estilo
 """
from flask import Flask, jsonify, request

app = Flask(__name__)
musicas = [
    {
        'Musica': "Ilusao 'Cracolandia'",
        'Estilo': 'Trap Funk'
    },
    {
        'Musica': "Set DJ Pedro 5.0",
        'Estilo': 'Funk'
    },
    {
        'Musica': "Gimme That",
        'Estilo': 'Hip Hop'
    },
    {
        'Musica': "Played Yourself",
        'Estilo': 'Hip Hop'
    },
]

# GET
@app.route('/musicas')
def obter_cancoes():
    return jsonify(musicas)

# GET com indice
@app.route('/musicas/<int:id>',methods=['GET'])
def obter_indice_id(id):
    return jsonify(musicas[id])


# POST
@app.route('/musicas',methods=['POST'])
def publicar_musica():
    musica = request.get_json()
    musicas.append(musica)
    return jsonify(musicas, 200)

# PUT
@app.route('/musicas/<int:id>',methods=['PUT'])
def editar_musica(id):
    musica_editada = request.get_json()
    musicas[id].update(musica_editada)
    return jsonify(musicas[id], 200)

# DELETE
@app.route('/musicas/<int:id>', methods=['DELETE'])
def deletar_musica(id):
    try:
        if musicas[id] is not None:
            del musicas[id]
            return jsonify(f'Musica {musicas[id]} deletado', 200)
    except:
        return jsonify(f'Não foi possivel deletar a musica {musicas[id]}', 404)

app.run(port=5000,host='localhost',debug=True)
