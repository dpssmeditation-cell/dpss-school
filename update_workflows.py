import os
import glob

# We need to extract the target time from the filename or yaml content.
# e.g., schedule_630am.yml -> target time is 06:30
# schedule_4pm.yml -> target time is 16:00
# schedule_1210pm.yml -> target time is 12:10

target_times = {
    'schedule_630am.yml': '06:30',
    'schedule_receptionist_640am.yml': '06:40',
    'schedule_wednesday_720am.yml': '07:20',
    'schedule_10am.yml': '10:00',
    'schedule_receptionist_1130am.yml': '11:30',
    'schedule_1210pm.yml': '12:10',
    'schedule_receptionist_150pm.yml': '13:50',
    'schedule_4pm.yml': '16:00',
    'schedule_friday_7am.yml': '07:00',
    'schedule_sunday_7am.yml': '07:00',
}

new_crons = {
    'schedule_630am.yml': '45 22 * * 0-4',
    'schedule_receptionist_640am.yml': '55 22 * * 0-4',
    'schedule_wednesday_720am.yml': '35 23 * * 2',
    'schedule_10am.yml': '15 2 * * 1-5',
    'schedule_receptionist_1130am.yml': '45 3 * * 1-5',
    'schedule_1210pm.yml': '25 4 * * 1-5',
    'schedule_receptionist_150pm.yml': '5 6 * * 1-5',
    'schedule_4pm.yml': '15 8 * * 1-5',
    'schedule_friday_7am.yml': '15 23 * * 4',
    'schedule_sunday_7am.yml': '15 23 * * 6',
}

files = glob.glob('/Users/macmini/dpss-school/.github/workflows/*.yml')

for filepath in files:
    filename = os.path.basename(filepath)
    if filename not in target_times:
        continue
        
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Replace cron line
        if '- cron:' in line:
            indent = line[:line.find('-')]
            out.append(f"{indent}- cron: '{new_crons[filename]}'\n")
            i += 1
            continue
            
        # Add env block to python run step
        if 'run: python3 scripts/' in line:
            out.append(line)
            indent = line[:line.find('run:')]
            out.append(f"{indent}env:\n")
            out.append(f"{indent}  TZ: \"Asia/Phnom_Penh\"\n")
            out.append(f"{indent}  TARGET_TIME: \"{target_times[filename]}\"\n")
            if 'receptionist' in filename:
                out.append(f"{indent}  RECEPTIONIST_BOT_TOKEN: ${{{{ secrets.RECEPTIONIST_BOT_TOKEN }}}}\n")
            else:
                out.append(f"{indent}  BOT_TOKEN: ${{{{ secrets.BOT_TOKEN }}}}\n")
            i += 1
            continue
            
        out.append(line)
        i += 1
        
    with open(filepath, 'w') as f:
        f.writelines(out)

print("All workflows updated with new crons and env vars.")
