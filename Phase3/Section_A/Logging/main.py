import logging

logging.basicConfig(
    filename='pokemon.log',
    level=logging.DEBUG,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug('The pokemon manager started')
logging.info('pikachu data loaded')
logging.warning('pokemon data files not found')
logging.error('pokemon files are currupted')
logging.critical('Pokemon project creashing')