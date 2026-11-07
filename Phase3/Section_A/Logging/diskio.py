import time
import psutil

disk_io = psutil.disk_io_counters()
read_count = disk_io.read_count
read_bytes = disk_io.read_bytes
write_count = disk_io.write_count
write_bytes = disk_io.write_bytes

# print(f'The count of reading : {read_count}')
# print(f'The bytes of data read : {read_bytes}')
# print('\n')
# print(f'The count of writen : {write_count}')
# print(f'The bytes of data written : {write_bytes}')

time.sleep(5)
disk_io2 = psutil.disk_io_counters()
read_count2 = disk_io2.read_count
read_bytes2 = disk_io2.read_bytes
write_count2 = disk_io2.write_count
write_bytes2 = disk_io2.write_bytes

print(f'The count of reading : {read_count2 - read_count}')
print(f'The bytes of data read : {read_bytes2 - read_bytes}')
print('\n')
print(f'The count of writen : {write_count2 - write_count}')
print(f'The bytes of data written : {write_bytes2 - write_bytes}')