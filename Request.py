import requests
import json

url = 'https://api.gdc.cancer.gov/files'
headers = {
    'Content-Type': 'application/json'
}
data = open('request.json', 'rb')

request = requests.post(url, data=data, headers=headers)

print(request)

responseFile = open('response.json', 'w')
responseFile.write(request.text)
