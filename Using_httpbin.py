import requests

# payload = {'page' : 2, 'count' : 25}
# r = requests.get('https://httpbin.org', params=payload)
# print(r.text)
# print(r.url)

# payload = {'username' : 'Rachit', 'password' : 'ketan@123'}
# r = requests.post('https://httpbin.org/post', data=payload)
# # print(r.text)
# print(r.url)
# print(r.json())

r = requests.get('http://httpbin.org/basic-auth/rachit/ketan@123', auth=('rachit', 'ketan@123'))
print(r.text)

