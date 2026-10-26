import psutil
n = 20
while n>0:
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f'CPU Usage : {cpu_usage}')
    n = n-1
    