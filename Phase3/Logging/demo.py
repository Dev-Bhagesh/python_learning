import psutil
import time

# bytes_size = 12000
# elapsed_time = 3

# read_speed = bytes_size/elapsed_time
# print(f'Read speed {read_speed} byte/seconds')

disk_io = psutil.disk_io_counters()
read_byts = disk_io.read_bytes
read_counts = disk_io.read_count
write_byts = disk_io.write_bytes
write_counts = disk_io.write_count

tim = 6
time.sleep(tim)

disk_io2 = psutil.disk_io_counters()
read_byts2 = disk_io2.read_bytes
read_counts2 = disk_io2.read_count
write_byts2 = disk_io2.write_bytes
write_counts2 = disk_io2.write_count

print(f'Total bytes read in given time : {read_byts2 - read_byts}')
print(f'Read speed : {(read_byts2 - read_byts) / tim}')
print(f'Write speed : {(write_byts2 - write_byts)/tim}')