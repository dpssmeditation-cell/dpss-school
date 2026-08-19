import urllib.request
import json
import datetime
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import telegram_utils

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID", "-1769054756")

today_date = datetime.datetime.now().strftime("%d/%m/%y")

# TODO: Fill in the content for messages 2 and 3
MESSAGE_TEMPLATE_1 = f"""<b>Head Teachers-- English FT teachers- Weekly meeting Thursday {today_date}</b> from 1A-Pre2AII, please drop your meeting information here by 10:00am tomorrow."""

MESSAGE_TEMPLATE_2 = f"""<b>Head Teachers-- English FT teachers- Weekly meeting Thursday {today_date}</b> from 2A-5B, please drop your meeting information here by 10:00am tomorrow."""

MESSAGE_TEMPLATE_3 = f"""<b>Head Teachers-Dear all assistant teachers.Weekly meeting Thursday {today_date}</b> for Morning shift, afternoon shift,and evening shift, please drop your meeting information here by 10:00am tomorrow."""

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data.get("ok", False)
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    for msg in [MESSAGE_TEMPLATE_1, MESSAGE_TEMPLATE_2, MESSAGE_TEMPLATE_3]:
        num = telegram_utils.get_next_number()
        success = send_message(f"{num}) {msg}")
        print(f"Message {num}: {'OK' if success else 'FAILED'}")
