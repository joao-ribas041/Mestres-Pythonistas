# Logging
import logging
'''
-debug - Só estou informando informações para desenvolvedores
- info - Só quero informar algo que está acontecendo no programa, mas que não é um erro.
- warning - Quero alertar sobre algo que está acontecendo, possívelmente fora do esperado,
    porém ainda não é um erro, mas pode gerar um futuramente.
- error - Um erro ocorreu na aplicação
- critical - Um erro com consequências graves acaba de ocorrer na aplicação.
'''
logging.basicConfig(level=logging.DEBUG, filename='app.log',filemode='a',format='%(levelname)s - %(message)s ') # Setar o nível
logging.debug('Logging no nível debug')
logging.info('Logging no nível info')
logging.warning('Logging no nível warning')
logging.error('Logging no nível error')
logging.critical('Logging no nível critical')