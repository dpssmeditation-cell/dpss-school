import json
import datetime
import os

COUNTER_FILE = os.path.join(os.path.dirname(__file__), '..', 'counter.json')

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

    try:
        with open(COUNTER_FILE, "w") as f:
            json.dump({"date": today, "count": count}, f)
    except Exception as e:
        print(f"Failed to update counter: {e}")

    return count
