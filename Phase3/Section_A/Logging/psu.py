import psutil

proc_list = []
for process in psutil.process_iter(['pid','name','memory_info']):
    try:
        # ram_info = process.memory_info().rss/(1024*1024)
        # print(f"PID : {process.info['pid']} | Process Name : {process.info['name']} | Memory Info : {ram_info:.2f} MB")

        proc_list.append(process)

    except psutil.NoSuchProcess as error:
        print(f'No Such Process Found : {error.pid} | {error.name}')
    except psutil.AccessDenied as error:
        print(f'AccessDenied For This Process : {error.pid} | {error.name}')

proc_list.sort(key=lambda process: process.info['memory_info'].rss,reverse=True)
print(proc_list[1])
print(proc_list[2])
print(proc_list[3])
print(proc_list[4])
print(proc_list[5])