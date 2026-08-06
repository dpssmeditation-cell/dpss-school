import urllib.request
import json
import datetime
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import telegram_utils

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8561116340:AAHcJyudj3FhFolhAnNIFt8I76WcdQjXtH8")
CHAT_ID = os.environ.get("CHAT_ID", "-1001769054756")

MESSAGE_TEMPLATE_1 = """Pha & Derith: FT Drop your weekly teaching plans. 2A-5B.

Deadline: Before 11:00 PM."""

MESSAGE_TEMPLATE_2 = """Chanthy: FT Drop your Weekly Plan and Daily Teaching Notes. 1A-PreAII.

Deadline: 9:30 AM."""

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
    for msg in [MESSAGE_TEMPLATE_1, MESSAGE_TEMPLATE_2]:
        num = telegram_utils.get_next_number()
        success = send_message(f"{num}) {msg}")
        print(f"Message {num}: {'OK' if success else 'FAILED'}")
