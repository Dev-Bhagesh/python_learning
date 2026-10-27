# import psutil

# for item in psutil.process_iter(['pid','name']):
#     print(item.info)

import psutil
from collections import defaultdict

usage = defaultdict(float)
for p in psutil.process_iter(['name', 'memory_info']):
    try:
        usage[p.info['name']] += p.info['memory_info'].rss / (1024 ** 2)
    except (psutil.NoSuchProcess, psutil.AccessDenied, TypeError):
        pass

for name, mb in sorted(usage.items(), key=lambda x: x[1], reverse=True)[:15]:
    print(f"{name:35} {mb:8.1f} MB")
    