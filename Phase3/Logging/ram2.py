import psutil

for item in psutil.process_iter(['pid','name']):
    print(item.info)
