import requests
dict1 = {}
list1 = []
list2 = []
responsec1 = requests.get(f"https://restcountries.com/v3.1/all?fields=name,capital")
responsecountry1 = responsec1.json()
print(responsecountry1)
for item in responsecountry1:
    list1.append(item["name"]["common"])
    list2.append(item["capital"])


