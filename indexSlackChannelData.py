import json
from bulkIndexDocument import makeBulkRequest

with open('sampleSlackChannel.json', 'r') as file:
    data = json.load(file)

# Index each message as a separate document 

messages = data["messages"]

makeBulkRequest('dashathonslackdata', messages)


