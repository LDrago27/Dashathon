import json
import random
from datetime import datetime, timedelta

# Function to generate a random timestamp between now and 6 months ago
def random_timestamp():
    now = datetime.now()
    six_months_ago = now - timedelta(days=180)
    random_date = six_months_ago + timedelta(seconds=random.randint(0, int((now - six_months_ago).total_seconds())))
    return int(random_date.timestamp())

# Read the existing JSON file
with open('slack_messages_contextual.json', 'r') as file:
    data = json.load(file)

newMessage = []
# Update timestamps for all messages
for message in data:
    new_timestamp = random_timestamp()
    message['ts'] = f"{new_timestamp}.{random.randint(0, 999999):06d}"
    
    # Update attachment timestamp if it exists
    if 'attachments' in message:
        for attachment in message['attachments']:
            if 'ts' in attachment:
                attachment['ts'] = new_timestamp

    # Update latest_reply if it exists
    if 'latest_reply' in message:
        reply_timestamp = random_timestamp()
        while reply_timestamp < float(message['ts'].split('.')[0]):
            reply_timestamp = random_timestamp()
        message['latest_reply'] = f"{reply_timestamp}.{random.randint(0, 999999):06d}"
    
    newMessage.append(message)

with open('sampleSlackChannel.json', 'r') as file:
    newData = json.load(file)

newData['messages'] = newData['messages'] + newMessage

with open('combinedSlackData.json', 'w', encoding='utf-8') as f:
    json.dump(newData, f, ensure_ascii=False, indent=4)