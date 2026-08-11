import json
import datetime
import os
import time

COUNTER_FILE = os.path.join(os.path.dirname(__file__), '..', 'counter.json')

def wait_for_target_time():
    target_time_str = os.environ.get("TARGET_TIME")
    if not target_time_str:
        return
        
    try:
        now = datetime.datetime.now()
        target_time = datetime.datetime.strptime(target_time_str, "%H:%M").time()
        target_datetime = datetime.datetime.combine(now.date(), target_time)
        
        # If the target time has already passed today, don't sleep
        if now >= target_datetime:
            print(f"Current time {now.strftime('%H:%M:%S')} is at or past target time {target_time_str}. Proceeding immediately.")
            return
            
        sleep_seconds = (target_datetime - now).total_seconds()
        print(f"Current time is {now.strftime('%H:%M:%S')}. Waiting {sleep_seconds:.1f} seconds until exactly {target_time_str}:00...")
        time.sleep(sleep_seconds)
        print(f"Wait complete! It is now {datetime.datetime.now().strftime('%H:%M:%S')}. Proceeding.")
    except Exception as e:
        print(f"Error parsing or waiting for target time: {e}")

def get_next_number():
    wait_for_target_time()
    
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    count = 1

    if os.path.exists(COUNTER_FILE):
        try:
            with open(COUNTER_FILE, "r") as f:
                data = json.load(f)
                if data.get("date") == today:
                    count = data.get("count", 0) + 1
        except Exception:
            pass

    try:
        with open(COUNTER_FILE, "w") as f:
            json.dump({"date": today, "count": count}, f)
    except Exception as e:
        print(f"Failed to update counter: {e}")

    return count
