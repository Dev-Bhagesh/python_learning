from datetime import datetime
from pathlib import Path

script_dir = Path(__file__).resolve().parent
log_file = script_dir / 'schedular_test.log'

with log_file.open('a', encoding='utf-8') as file:
    file.write(f'Script run on time {datetime.now()}\n')

print('Script run success')