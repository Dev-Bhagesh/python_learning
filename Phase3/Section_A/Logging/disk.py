import psutil

disk = psutil.disk_usage("C:\\")
free = disk.free/(1024**3)
total = disk.total/(1024**3)
percent = disk.percent
used = disk.used/(1024**3)
print(f'Total Space : {total:.2f} Gb')
print(f'Free Space : {free:.2f} GB')
print(f'Used Space : {used:.2f} GB')
if percent>90:
    print(f'Percent : {percent}%')
    print('Disk is overloading')
else:
    print(f'Percent : {percent}%')
    print('Disk is in good condition')