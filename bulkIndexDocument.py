import requests
from requests.auth import HTTPBasicAuth
import json

def getClusterConfig():
    with open('config.json', 'r') as file:
        config = json.load(file)

    return [config.get('userName') , config.get('passWord'), config.get('bulkOSUrl')]

def createBulkIndexDocumentBody(indexName: str, docArray):

    bulkBody = []

    for doc in docArray:
        metaData = { "index": { "_index": indexName } }
        bulkBody.append(metaData)
        bulkBody.append(doc)

    return '\n'.join([json.dumps(line) for line in bulkBody]) + '\n'

def makeBulkRequest(indexName: str, docArray):

    userName, passWord, url = getClusterConfig()

    reqBody = createBulkIndexDocumentBody(indexName, docArray)

    response = requests.post(url, data=reqBody, headers={"Content-Type": "application/json"}, auth=HTTPBasicAuth(userName, passWord))

    print(json.dumps(response.json()))




    

