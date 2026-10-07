import requests

response = requests.get("https://aparateka.shop/product?id=694")
print(response.status_code)
print(response.text)