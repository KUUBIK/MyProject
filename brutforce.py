import requests


url = 'http://192.168.1.1'
payload = {
    'inUserName': 'admin',
    'inUserPass': 'FUGAS190998'
}

s = requests.Session()
r = requests.post('http://localhost:9999/', data=payload)

print(r.text)


# session.headers.update({"request_header1": "request_value1"})
# params = {"param1": "value1"}
# session.post("https://site.com", data=params)
