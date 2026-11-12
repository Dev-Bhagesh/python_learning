import requests

url = 'http://127.0.0.1:8000/Get-key'
print(url)
response = requests.get(
    # url = f'{url}/Get-key'
    url
)


print(response.json())
print(response.json()['key'])

header = {
    # 'x-api-key':response.json()['key']
    'x-api-key':'hi_i_am'
}

url = 'http://127.0.0.1:8000/protected'
response2 = requests.get(
    url,
    headers=header
)

print(response2.json())