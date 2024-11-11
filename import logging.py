import logging
import getpass

# Configuración básica del logger
logging.basicConfig(filename='mi_scriptttt.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def mi_funcion():
    usuario = getpass.getuser()
    logger.info(f'El usuario {usuario} ha iniciado la función')
    try:
        # Código de tu función
        resultado = 10 / 2
        logger.info(f'El resultado es {resultado}')
    except Exception as e:
        logger.error(f'Error encontrado: {e}')
    logger.info(f'El usuario {usuario} ha terminado la función')

if __name__ == '__main__':
    usuario = getpass.getuser()
    logger.info(f'El usuario {usuario} ha iniciado el script')
    mi_funcion()
    logger.info(f'El usuario {usuario} ha terminado el script')
