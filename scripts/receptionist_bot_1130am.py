import urllib.request
import json
import datetime
import os

BOT_TOKEN = os.environ.get("RECEPTIONIST_BOT_TOKEN")
CHAT_ID = os.environ.get("RECEPTIONIST_CHAT_ID", "-1001554726520")

today_date = datetime.datetime.now().strftime("%d.%m.%Y")

MESSAGE_TEMPLATE = f"""5).<b>Absent FT&Khmer Students - Afternoon Shift ({today_date}).</b> Please write absent/late students in the comment below."""

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
    success = send_message(MESSAGE_TEMPLATE)
    print(f"Message 5: {'OK' if success else 'FAILED'}")
