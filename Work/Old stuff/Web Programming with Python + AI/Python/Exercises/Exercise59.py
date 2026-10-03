import requests

a = input("Enter a country : ")
b = input("Enter some text : ")

response3 = requests.get(f"https://restcountries.com/v3.1/name/{a}")
response1 = response3.json()

TOKEN = "8527869906:AAGa4akV61S0FCyfxSyL5qpy81mISVr1jA8"
CHAT_ID = "-5294797892"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
url2 = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
params = {"chat_id": CHAT_ID, "text": response1[0]["name"]["common"]}
params2 = {"chat_id": CHAT_ID, "photo": response1[0]["flags"]["png"]}
params3 = {"chat_id": CHAT_ID, "text": b}
response = requests.post(url, params=params)
response2 = requests.post(url2, params=params2)
response3 = requests.post(url, params=params3)
print(response.json())
print(response2.json())
print(response3.json())