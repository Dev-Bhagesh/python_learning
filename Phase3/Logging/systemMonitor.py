import psutil
import logging
from logging.handlers import RotatingFileHandler
import time

tim = 5

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
print(f'='*10,' CPU ','='*10)
cpu_sec = psutil.cpu_percent(interval=1)
print(f'CPU Usage : {cpu_sec}%')
print('='*40)

#RAM section
print(f'='*10,' RAM ','='*10)
ram_sec = psutil.virtual_memory()
availabe_ram = ram_sec.available
used_ram = ram_sec.used
total_ram = ram_sec.total
# ram_usage = ram_sec.usage
print(f'Total RAM : {(ram_sec.total)/(1024**3) :.2f} GiB ')
print(f'Availabe RAM : {(ram_sec.available)/(1024**3) :.2f} GiB')
print(f'Percentage Used : {(ram_sec.percent)}%')
print(f'Free RAM : {(ram_sec.free)/(1024**3) :.2f} GiB')
print('='*40)

#Process Section
print(f'='*10,' Processes ','='*10)
Processes = []
for process in psutil.process_iter(['pid','name','memory_info']):
    Processes.append(process)

Processes.sort(key=lambda item: item.info['memory_info'].rss,reverse=True)
for item in Processes[:5]:
    name = item.info['name']
    byte_ram = item.info['memory_info'].rss
    ram_MB = byte_ram/(1024*1024)

    print(f'{name} : {ram_MB :.2f} MB')
print('='*40)

# Disk Sapce
print(f'='*10,' Disk ','='*10)
c_disk = psutil.disk_usage('C:\\')
print(f'Total Disk Space : {(c_disk.total)/(1024**3) :.2f} GB')
print(f'Used Space : {(c_disk.used)/(1024**3) :.2f} GB')
print(f'Free Space : {(c_disk.free)/(1024**3) :.2f} GB')
print(f'Percent : {c_disk.percent}%')
print('='*40)

# Disk IO
print(f'='*10,' Disk IO ','='*10)
disk = psutil.disk_io_counters()
disk_byte_read = disk.read_bytes
disk_byte_write = disk.write_bytes

start = time.perf_counter()
time.sleep(tim)
elipsed_time = time.perf_counter() - start

disk2 = psutil.disk_io_counters()
disk_byte_read2 = disk2.read_bytes
disk_byte_write2 = disk2.write_bytes

disk_bytes_readMB = (disk_byte_read2 - disk_byte_read) / (1024*1024)
disk_bytes_writeMB = (disk_byte_write2 - disk_byte_write) / (1024*1024)

disk_read_speed = disk_bytes_readMB / elipsed_time
disk_write_speed = disk_bytes_writeMB / elipsed_time

print(f'The Bytes Read in given time : {disk_bytes_readMB :.2f} MB')
print(f'The Bytes written in given time : {disk_bytes_writeMB :.2f} MB')
print(f'The disk Read Speed : {disk_read_speed :.2f} MB/s')
print(f'The disk Write Speed : {disk_write_speed :.2f} MB/s')
print('='*40)

#Network IO
print(f'='*10,' Network IO ','='*10)
netIO = psutil.net_io_counters()
net_byte_read = netIO.bytes_recv
net_byte_write = netIO.bytes_sent

start = time.perf_counter()
time.sleep(tim)
elipsed_time = time.perf_counter() - start

netIO2 = psutil.net_io_counters()
net_bytes_read2 = netIO2.bytes_recv
net_bytes_write2 = netIO2.bytes_sent

net_bytes_readMB = (net_bytes_read2 - net_byte_read) / (1024*1024)
net_bytes_writeMB = (net_bytes_write2 - net_byte_write) / (1024*1024)

net_bytes_read_speed = net_bytes_readMB / elipsed_time
net_bytes_write_speed = net_bytes_writeMB / elipsed_time

print(f'The data recived on network in give time : {net_bytes_readMB :.2f} MB')
print(f'The data sent on the eetwork in given time : {net_bytes_writeMB :.2f} MB')
print(f'The Download speed : {net_bytes_read_speed :.2f} MB/s')
print(f'The Upload Speed : {net_bytes_write_speed :.2f} MB/s')