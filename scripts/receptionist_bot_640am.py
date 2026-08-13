import urllib.request
import json
import datetime
import os

BOT_TOKEN = os.environ.get("RECEPTIONIST_BOT_TOKEN")
CHAT_ID = os.environ.get("RECEPTIONIST_CHAT_ID", "-1001554726520")

today_date = datetime.datetime.now().strftime("%d.%m.%Y")

MESSAGE_TEMPLATE_1 = f"""1). <b>Absent FT&Khmer Students - Morning Shift ({today_date}).</b> Please write absent/late students in the comment below."""

MESSAGE_TEMPLATE_2 = f"""2).Document Copies 
Full-time <b>({today_date})</b>. 
Please attach yrs to-be-copied files in the comment below before 03:00pm.  
Please list down : 
⁃ Class time
⁃ Number of Copy
⁃ Date to use 
⁃ level  
<b>សូមលោកគ្រូអ្នកគ្រូជួយ Edit នៅចុងសន្លឹកទី១ ដាក់ឈ្មោះ កម្រិត ចំនួននិងថ្ងៃផង។ដើម្បីសម្រួលដល់ការច្រឡំក្រដាសគ្នា។
Note: សូមលោកគ្រូ-អ្នកគ្រូជួយកែឈ្មោះ file ផង
Example: Level_Name&Name_(…..)</b>
Thanks!"""

MESSAGE_TEMPLATE_3 = f"""3).<b>Document Copies 
Part-Time ({today_date})</b>. 
Please attach yrs to-be-copied files in the comment below before <b>03:00pm.</b>  
Please list down : 
⁃ Class time
⁃ Number of Copy
⁃ Date to use 
⁃ level  
<b>សូមលោកគ្រូអ្នកគ្រូជួយEdit នៅចុងសន្លឹកទី១ ដាក់ឈ្មោះ កម្រិត ចំនួននិងថ្ងៃផង។ដើម្បីសម្រួលដល់ការច្រឡំក្រដាសគ្នា។
Note: សូមលោកគ្រូ-អ្នកគ្រូជួយកែឈ្មោះ file ផង
Example: Level_Name&Name_(…..)</b>
Thanks!"""

MESSAGE_TEMPLATE_4 = f"""4).<b>Document Copies 
Khmer ({today_date}).</b> 
Please attach yrs to-be-copied files in the comment below before <b>03:00pm.</b>  
Please list down : 
⁃ Class time
⁃ Number of Copy
⁃ Date to use 
⁃ level  
<b>សូមលោកគ្រូអ្នកគ្រូជួយEdit នៅចុងសន្លឹកទី១ ដាក់ឈ្មោះ កម្រិត ចំនួននិងថ្ងៃផង។ដើម្បីសម្រួលដល់ការច្រឡំក្រដាសគ្នា។
Note: សូមលោកគ្រូ-អ្នកគ្រូជួយកែឈ្មោះ file ផង
Example: Level_Name&Name_(…..)</b>
Thanks!"""

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
    for i, msg in enumerate([MESSAGE_TEMPLATE_1, MESSAGE_TEMPLATE_2, MESSAGE_TEMPLATE_3, MESSAGE_TEMPLATE_4], 1):
        success = send_message(msg)
        print(f"Message {i}: {'OK' if success else 'FAILED'}")
