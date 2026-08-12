import urllib.request
import urllib.parse
import json
import datetime
import sys
import telegram_utils

BOT_TOKEN = "8561116340:AAHcJyudj3FhFolhAnNIFt8I76WcdQjXtH8"
CHAT_ID = "-1001769054756" 
FALLBACK_CHAT_ID = "-1769054756"

# Generate today's date
today_date = datetime.datetime.now().strftime("%B %-d, %Y") # e.g. August 4, 2026

MESSAGE_TEMPLATE_1 = f"""Pha & Derith- Morning English FT - info about meeting from 2A-5B. ({today_date})
 
Note: Please comment "Noted" after listening.
 
Thanks"""

MESSAGE_TEMPLATE_2 = f"""Chanthy- Morning and English FT - info about meeting from 1A-Pre2A. ({today_date})
 
Note: Please comment "Noted" after listening.
 
Thanks"""

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            if res_data.get("ok"):
                log(f"Message sent successfully to {chat_id}!")
                return True
            else:
                log(f"Failed to send to {chat_id}: {res_data}")
                return False
    except urllib.error.HTTPError as e:
        error_info = e.read().decode('utf-8')
        log(f"HTTPError {e.code} when sending to {chat_id}: {error_info}")
        return False
    except Exception as e:
        log(f"Exception when sending to {chat_id}: {e}")
        return False

def log(msg):
    print(msg)
    with open("/Users/macmini/Documents/DPSS Telegram/bot_10am.log", "a") as f:
        f.write(f"{datetime.datetime.now()}: {msg}\n")

if __name__ == "__main__":
    messages = [MESSAGE_TEMPLATE_1, MESSAGE_TEMPLATE_2]
    
    for idx, msg in enumerate(messages):
        num = telegram_utils.get_next_number()
        numbered_msg = f"{num}) {msg}"
        log(f"Sending 10 AM message {idx+1} (Numbered {num})...")
        success = send_message(CHAT_ID, numbered_msg)
        if not success:
            log("Trying fallback chat ID...")
            success = send_message(FALLBACK_CHAT_ID, numbered_msg)
        
        if not success:
            log(f"Failed to send message {idx+1}.")
        else:
            log(f"Message {idx+1} successfully sent!")
