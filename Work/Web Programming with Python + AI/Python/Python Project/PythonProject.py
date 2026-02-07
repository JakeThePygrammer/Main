import requests

print("Option 1 - country information")
print("Option 2 - country comparison")
print("Option 3 - quiz")
print("Option 4 - search history")
options = input("Choose one(enter the corresponding number) : ")

if options == "1":
    name = input("Enter a country : ")
    response = requests.get(f"https://restcountries.com/v3.1/name/{name}")
    response1 = response.json()
    if response.status_code == 404:
        print("The country you have entered does not exist!")
    if response.status_code == 200:
        print(f"Name : {response1[0]["name"]["common"]}")
        print(f"Capital : {response1[0]["capital"][0]}")
        print(f"Continent : {response1[0]["continents"][0]}")
        print(f"Population : {response1[0]["population"]}")
        a = list(response1[0]["currencies"].keys())
        print(f"Currency : {a[0]} - {response1[0]["currencies"][a[0]]["name"]}")
        print(f"Flag : {response1[0]["flags"]["png"]}")

if options == "2":
    name1 = input("Enter country 1 : ")
    responsec1 = requests.get(f"https://restcountries.com/v3.1/name/{name1}")
    responsecountry1 = responsec1.json()
    name2 = input("Enter country 2 : ")
    responsec2 = requests.get(f"https://restcountries.com/v3.1/name/{name2}")
    responsecountry2 = responsec2.json()
    if responsec1.status_code == 404 or responsec2.status_code == 404:
        print("The country you have entered does not exist!")
    if responsec1.status_code == 200 and responsec2.status_code == 200:
        if responsecountry1[0]["population"] > responsecountry2[0]["population"]:
            print(f"{responsecountry1[0]["name"]["common"]} has a bigger population than {responsecountry2[0]["name"]["common"]}.")
        elif responsecountry2[0]["population"] > responsecountry1[0]["population"]:
            print(f"{responsecountry2[0]["name"]["common"]} has a bigger population than {responsecountry1[0]["name"]["common"]}.")
        else:
            print("Both countries have an equal population.")

if options == 3:
