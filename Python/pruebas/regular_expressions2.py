

import re

log_entry_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\w+) - (.+)')

# Replace 'sample_log.txt' with the actual name of your log file
log_file_path = 'texto.txt'

with open(log_file_path, 'r') as file:
    for line in file:
        match = log_entry_pattern.match(line)
        if match:
            timestamp, log_level, log_message = match.groups()
            print(f'Timestamp: {timestamp}, Level: {log_level}, Message: {log_message}')














