import json
from bulkIndexDocument import makeBulkRequest

with open('issues.json', 'r') as file:
    data = json.load(file)

# Index each message as a separate document 
docArray = []
for key in data:
    docArray.append(data[key])

makeBulkRequest('dashathongithubdata', docArray)