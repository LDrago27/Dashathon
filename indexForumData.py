import json
from bulkIndexDocument import makeBulkRequest

with open('forum-data.json', 'r') as file:
    data = json.load(file)

# Index each message as a separate document 

makeBulkRequest('dashathonforumdata', data)


