import requests

number = int(input("How many cat facts would you like : "))

for index in range(number):
    response = requests.get("https://catfact.ninja/fact")
    response1 = response.json()
    print(f"Cat fact number {index+1} : {response1["fact"]}")

