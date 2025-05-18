import requests
import json

url = 'http://localhost:8000/api/users/register/'
headers = {
    'Content-Type': 'application/json'
}
data = {
    'username': 'test2',
    'email': 'test2@example.com',
    'password': 'testpass123'
}

response = requests.post(url, headers=headers, json=data)
print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}') 