import requests

r = requests.get('https://api.github.com/events')

#print r.text


payload = {'key1': 'value1', 'key2': 'value2'}



r2 = requests.post('http://httpbin.org/post', data=payload)

print r2.text
