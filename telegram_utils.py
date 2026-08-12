import json
import os
import datetime

COUNTER_FILE = "/Users/macmini/Documents/DPSS Telegram/counter.json"

def get_next_number():
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
            
    # Save the new count
    try:
        with open(COUNTER_FILE, "w") as f:
            json.dump({"date": today, "count": count}, f)
    except Exception:
        pass
        
    return count
