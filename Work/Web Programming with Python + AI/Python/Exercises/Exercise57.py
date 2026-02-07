import requests

list1 = []

for index in range(5):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    response1 = response.json()
    print(response1["setup"])
    a = input()
    print(response1["punchline"])
    print("Did you like this joke(Y/N) : ")
    a1 = input()
    if a1.lower() == "y":
        list1.append(response1["setup"] + " " + response1["punchline"])

print("Your liked jokes : ")
for item in list1:
    print(item)