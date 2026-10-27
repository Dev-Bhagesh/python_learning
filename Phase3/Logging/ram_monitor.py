import time
import logging
from logging.handlers import RotatingFileHandler
import psutil

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)

handler = RotatingFileHandler(
    filename='RAM_MONITORING.log',
    maxBytes=1024*1024,
    backupCount=3,
    encoding='utf-8'
)

handler.setFormatter(formatter)
logger.addHandler(handler)

count = 0
while 1:
    try:
        ram_ = psutil.virtual_memory()
        logger.info(f'Total RAM : {ram_.total/(1024 ** 3)}')
        logger.info(f'Availabe RAM : {ram_.available/(1024 ** 3)}')
        logger.info(f'Total RAM Usage : {ram_.percent}%')
        logger.info(f'Total Free RAM : {ram_.free/(1024**3)}')
        logger.info(f'-'*30)
    except KeyboardInterrupt as error:
        logger.error('RAM Monitoring Stoped')
        break

    print(f'Log uploaded : {count}')
    time.sleep(5)
    count += 1