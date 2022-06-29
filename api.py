import requests

URL = "http://127.0.0.1:8000/student/"
data = {
    'name' : 'Rupesh Patra',
    'roll' : 103,
    'email' : 'rupesh@gmail.com',
    'city' : 'Surat'
}
req = requests.get(url=URL)
data = req.json()
print(data)