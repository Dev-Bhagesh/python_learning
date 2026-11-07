import os
os.environ['trainer'] = 'ash'
print(os.getenv('trainer'))
print(os.environ['trainer'])
os.environ['trainer'] = 'red'
print(os.getenv('trainer'))
os.environ.pop('trainer')
print(os.getenv('trainer'))