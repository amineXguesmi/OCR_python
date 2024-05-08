import requests

url = 'http://localhost:5000/ocr'
files = {'file': open('image.png', 'rb')}  
response = requests.post(url, files=files)

if response.status_code == 200:
    print(response.json())
else:
    print('Error:', response.text)