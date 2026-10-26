import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("BackupLogger")
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler(
    filename='backupLogger.log',
    maxBytes=200,
    backupCount=3,
    encoding='utf-8'
)

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("Backup utility initialized")
logger.info("Backup process started")
logger.warning("pika.json was not found")
# logger.error('this is a error')
logger.error("Failed to copy bulba.json")

logger.info("Backup process completed")