from http.server import executable
import sys
import os
from cx_Freeze import setup,  Executable

# Definir o que deve ser incluído na pasta final
arquivos =['web.ico','teste/'] 

# Saida de arquivos
configuracao = Executable(
    script='app.py',
    icon='web.ico'
)

# Configurar o cx-freeze(detalhes do programa)
setup(
    name='automatizador de Login',
    version='1.0',
    description='Este programa automatiza o login',
    author='Joao Ribas',
    options = {'buiild.exe': {'include_files': arquivos}},
    executables=[configuracao]
)