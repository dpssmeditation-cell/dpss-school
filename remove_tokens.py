import os
import glob

files = glob.glob('/Users/macmini/dpss-school/scripts/*.py')
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Replace bot tokens
    content = content.replace(
        'os.environ.get("BOT_TOKEN", "8561116340:AAHcJyudj3FhFolhAnNIFt8I76WcdQjXtH8")',
        'os.environ.get("BOT_TOKEN")'
    )
    content = content.replace(
        'os.environ.get("RECEPTIONIST_BOT_TOKEN", "8984514690:AAF4CM76QTDFgDKhugvSdTFYq6cV2a-lqy4")',
        'os.environ.get("RECEPTIONIST_BOT_TOKEN")'
    )
    
    with open(f, 'w') as file:
        file.write(content)

print("Tokens removed from all scripts.")
