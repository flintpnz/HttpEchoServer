import requests

r = requests.get('http://127.0.0.1:80', data='some GET payload')
print(r.text)

r = requests.post('http://127.0.0.1:80', data='some POST payload')
print(r.text)

r = requests.put('http://127.0.0.1:80', data='some PUT payload')
print(r.text)

r = requests.delete('http://127.0.0.1:80', data='some DELETE payload')
print(r.text)
