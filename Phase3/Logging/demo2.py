# import time
# import psutil

# diskIO = psutil.disk_io_counters()
# byts_read = diskIO.read_bytes
# byts_write = diskIO.write_bytes

# tim = 4
# start = time.perf_counter()
# time.sleep(tim)
# elapsed = time.perf_counter() - start

# diskIO2 = psutil.disk_io_counters()
# byts_write2 = diskIO2.write_bytes
# byts_read2 = diskIO2.read_bytes

# total_byts_read = byts_read2 - byts_read
# total_byts_write = byts_write2 - byts_write

# read_inMB = total_byts_read/(1024*1024)
# read_time = total_byts_read/(1024*1024)/elapsed

# write_inMB = total_byts_write/(1024*1024)
# write_time = total_byts_write/(1024*1024)/elapsed

# print(f'Total bytes read during the interval : {total_byts_read}')
# print(f'Total bytes written during the interval : {total_byts_write}')
# print(f'Read Data in MBs : {read_inMB} MB')
# print(f'Write Data in MBs : {write_inMB} MB')
# print(f'Read speed : {read_time}')
# print(f'Write speed : {write_time}')

import psutil
import time

tim = int(input('Enter the time in second : '))

disk = psutil.disk_io_counters()
byts_read = disk.read_bytes
byts_write = disk.write_bytes

start = time.perf_counter()
time.sleep(tim)
elapsed_time = time.perf_counter() - start

disk2 = psutil.disk_io_counters()
byts_read2 = disk2.read_bytes
byts_write2 = disk2.write_bytes

readMB = (byts_read2 - byts_read)/(1024*1024)
writeMB = (byts_write2 - byts_write)/(1024*1024)

read_speed = (byts_read2-byts_read)/(1024*1024)/elapsed_time
write_speed = (byts_write2 - byts_write)/(1024*1024)/elapsed_time

print(f' Bytes read : {readMB :.2f} MB')
print(f' Bytes Write : {writeMB :.2f} MB')
print(f' ReadSpeed : {read_speed :.2f} MB/s')
print(f' WriteSpeed : {write_speed :.2f} MB/s')
