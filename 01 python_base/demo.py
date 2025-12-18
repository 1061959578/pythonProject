import requests


a = []
print(a.append('a'))
print('------------------')
print(a)


response = requests.get('https://httpbin.org/get')
print(f"状态码: {response.status_code}")