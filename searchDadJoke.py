import requests

url = 'https://icanhazdadjoke.com/search'
headers = {
    'Accept': 'application/json'
}
params = {
    'term': 'dog',
    'limit': '5'
}
response = requests.get(url, headers=headers, params=params)
joke = response.json()
print(joke)