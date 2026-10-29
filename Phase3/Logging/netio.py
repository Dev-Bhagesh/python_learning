import psutil
import time

net_io = psutil.net_io_counters()

tim = int(input('Enter the time duration:'))

rec_bytes = net_io.bytes_recv
sent_bytes = net_io.bytes_sent

start_time = time.perf_counter()
time.sleep(tim)
elapsed_time = time.perf_counter() - start_time

net_io2 = psutil.net_io_counters()
rec_bytes2 = net_io2.bytes_recv
send_bytes2 = net_io2.bytes_sent

print(f'Total bytes recived during the interval : {(rec_bytes2 - rec_bytes)/(1024*1024) :.2f} MB')
print(f'Total bytes sent during the interval : {(send_bytes2 - sent_bytes)/(1024*1024) :.2f} MB')

print(f'Recive speed : {((rec_bytes2 - rec_bytes)/elapsed_time)/(1024*1024) :.2f} MB/s')
print(f'Upload speed : {((send_bytes2 - sent_bytes)/elapsed_time)/(1024*1024) :.2f} MB/s')