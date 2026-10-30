import psutil
import logging
from logging.handlers import RotatingFileHandler
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    filename='SystemLog.log',
    maxBytes=1024*1024,
    backupCount=3
)

formater = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)

handler.setFormatter(formater)
logger.addHandler(handler)

# CPU section
cpu_sec = psutil.cpu_percent(interval=1)
print(f'CPU Usage : {cpu_sec}%')

#RAM section
print('=======================================================================')
ram_sec = psutil.virtual_memory()
availabe_ram = ram_sec.available
used_ram = ram_sec.used
total_ram = ram_sec.total
# ram_usage = ram_sec.usage

print(f'Total RAM : {(ram_sec.total)/(1024**3) :.2f} GiB ')
print(f'Availabe RAM : {(ram_sec.available)/(1024**3) :.2f} GiB')
print(f'Percentage Used : {(ram_sec.percent)}%')
print(f'Free RAM : {(ram_sec.free)/(1024**3) :.2f} GiB')

#Process Section
print('=======================================================================')
Processes = []
for process in psutil.process_iter(['pid','name','memory_info']):
    Processes.append(process)

Processes.sort(key=lambda item: item.info['memory_info'].rss,reverse=True)
for item in Processes:
    name = item.info['name']
    byte_ram = item.info['memory_info'].rss
    ram_MB = byte_ram/(1024*1024)

    print(f'{name} : {ram_MB :.2f} MB')