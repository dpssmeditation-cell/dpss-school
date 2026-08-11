import urllib.request
import json
import datetime
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import telegram_utils

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID", "-1001769054756")

MESSAGE_TEMPLATE = """Head-Teachers- Dear English FT Teachers

Our weekly meeting will start at: 
<b>Morning shift: 8:00
Afternoon shift: 2:00</b>
Thank you."""

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data.get("ok", False)
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    num = telegram_utils.get_next_number()
    success = send_message(f"{num}) {MESSAGE_TEMPLATE}")
    print(f"Message {num}: {'OK' if success else 'FAILED'}")
