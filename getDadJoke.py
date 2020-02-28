import requests

url = 'https://icanhazdadjoke.com/'
headers = {
    'Accept': 'application/json'
}
response = requests.get(url, headers=headers)
joke = response.json()
print(joke)