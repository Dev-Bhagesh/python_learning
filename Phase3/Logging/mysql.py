import psutil

for p in psutil.process_iter(['pid', 'name', 'exe', 'cmdline', 'ppid']):
    if p.info['name'] and p.info['name'].lower() == 'mysqld.exe':
        print(p.info['pid'], 'parent:', p.info['ppid'])
        print('  exe:', p.info['exe'])
        print('  cmd:', p.info['cmdline'])