import urllib.request
import json
import datetime
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import telegram_utils

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID", "-1001769054756")

today_date = datetime.datetime.now().strftime("%B %-d, %Y")

MESSAGE_TEMPLATE_1 = f"""Sina - សិស្សយឺត អត់ខ្សែក្រវ៉ាត់ កាត ខុសទ្រនាប់ជើង និងឯកសណ្ឋាន វេនរសៀល {today_date}។ *សូមសន្តិសុខថតរូប សួរឈ្មោះសិស្ស រួចសរសេរឈ្មោះសិស្ស ពីក្រោមរូបភាពជាអក្សរ ឬសំឡេង ទំលាក់ក្នុងទីនេះ ហើយសូមលោកគ្រូអ្នកគ្រូចូលមើល
មុនផ្ញើឈ្មោះអ្នកអវត្តមាន អោយអ្នកផ្ដល់ព័ត៌មាន។* 
សូមអរគុណ!"""

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
    num = telegram_utils.get_next_number()
    success = send_message(f"{num}) {MESSAGE_TEMPLATE_1}")
    print(f"Message {num}: {'OK' if success else 'FAILED'}")
