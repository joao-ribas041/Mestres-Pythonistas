'''
# REGEX ou Regular Expression
* De forma geral, o regex é como se fosse uma forma de encontrar, substituir,
e extrair um único ou uma sequência de carácteres.'''
# CARACTERE - qualquer letra, dígito ou símbolo no padrão
import re

hey = 'carol@gmail.com.br'
# Findall
result = re.findall(r"(@.{1,8}\.)", hey)
print(result)

# Search
result = re.search(r"(@.{1,8}\.)", hey)
print(result)

# Split
result = re.split(r"(@.{1,8}\.)", hey)
print(result)

# Sub
result = re.sub(r"(@.{1,8}\.)", '@yahoo.', hey)
print(result)