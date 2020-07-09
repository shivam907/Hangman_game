import requests

url = "https://url-shortener-service.p.rapidapi.com/shorten"

payload = "url=https://youtube.com/CREATIVEEXPERTZ/channel"
headers = {
    'x-rapidapi-host': "url-shortener-service.p.rapidapi.com",
    'x-rapidapi-key': "2c8be93a48msh8a3e054ad37fb73p1d4f4bjsn7b1edb7b2798",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)
d=response.json()
print(d["result_url"])