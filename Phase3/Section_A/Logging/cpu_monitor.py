import logging
import time
import psutil
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler(
    filename='CPU_MONITORING.log',
    maxBytes=1024*1024,
    backupCount = 3,
    encoding = 'utf-8'
)

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)

handler.setFormatter(formatter)
logger.addHandler(handler)

while 1:
    try:
        cpu_usage = psutil.cpu_percent(interval=None)
        if cpu_usage<30:
            print(f'CPU Usage Low: {cpu_usage}%')
            logger.info(f'CPUT Usage Low : {cpu_usage}%')
        elif cpu_usage>30 and cpu_usage<70:
            print(f'CPU Usage Moderate: {cpu_usage}%')
            logger.info(f'CPUT Usage Moderate : {cpu_usage}%')
        elif cpu_usage>70 :
            print(f'CPU Usage High : {cpu_usage}%')
            logger.info(f'CPUT Usage High : {cpu_usage}%')

        time.sleep(5)
    except KeyboardInterrupt as error:
        print('Monitoring stopped')
        logger.error(f'Monitoring Stopper : {error}')
        break