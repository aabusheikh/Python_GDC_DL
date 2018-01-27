import requests
import json

url = 'https://api.gdc.cancer.gov/files'
headers = {
    'Content-Type': 'application/json'
}
data = open('request.json', 'rb')

r = requests.post(url, data=data, headers=headers)

print(r)
