import requests
import random

print("Option 1 - country information")
print("Option 2 - country comparison")
print("Option 3 - quiz")
print("Option 4 - search history")
print("Option 5 - borders")
print("Enter exit to exit")

while True:
    options = input("\nChoose one(enter the corresponding number) : ")

    if options == "1":
        name = input("\nEnter a country : ")
        response = requests.get(f"https://restcountries.com/v3.1/name/{name}")
        response1 = response.json()
        if response.status_code == 404:
            print("\nThe country you have entered does not exist!")
        if response.status_code == 200:
            print(f"\nName : {response1[0]["name"]["common"]}")
            print(f"Capital : {response1[0]["capital"][0]}")
            print(f"Continent : {response1[0]["continents"][0]}")
            print(f"Population : {response1[0]["population"]}")
            a = list(response1[0]["currencies"].keys())
            print(f"Currency : {a[0]} - {response1[0]["currencies"][a[0]]["name"]}")
            print(f"Flag : {response1[0]["flags"]["png"]}")
            print(f"Size : {response1[0]["area"]} km2")
            file = open("SearchText.txt", "a")
            file.write(f"{response1[0]["name"]["common"]} - {response1[0]["capital"][0]} - {response1[0]["continents"][0]}\n")
            file.close()
        continue

    if options == "2":
        name1 = input("\nEnter country 1 : ")
        responsec1 = requests.get(f"https://restcountries.com/v3.1/name/{name1}?fields=name,population")
        responsecountry1 = responsec1.json()
        name2 = input("Enter country 2 : ")
        responsec2 = requests.get(f"https://restcountries.com/v3.1/name/{name2}?fields=name,population")
        responsecountry2 = responsec2.json()
        if responsec1.status_code == 404 or responsec2.status_code == 404:
            print("\nThe country you have entered does not exist!")
        if responsec1.status_code == 200 and responsec2.status_code == 200:
            if responsecountry1[0]["population"] > responsecountry2[0]["population"]:
                print(
                    f"\n{responsecountry1[0]["name"]["common"]} has a bigger population than {responsecountry2[0]["name"]["common"]}.")
            elif responsecountry2[0]["population"] > responsecountry1[0]["population"]:
                print(f"\n{responsecountry2[0]["name"]["common"]} has a bigger population than {responsecountry1[0]["name"]["common"]}.")
            else:
                print("\nBoth countries have an equal population.")
        continue

    if options == "3":
        list1 = []
        list2 = []
        responsec1 = requests.get(f"https://restcountries.com/v3.1/all?fields=name,capital")
        responsecountry1 = responsec1.json()
        for item in responsecountry1:
            list1.append(item["name"]["common"])
            list2.append(item["capital"])

        counter = 0
        for index1 in range(5):
            guess = random.choice(list1)
            b = list2[list1.index(guess)][0]
            for index in range(3):
                a = input(f"What is the capital of {guess} : ")
                if a.lower() == b.lower():
                    print(f"Correct! The capital of {guess} is {b}!")
                    counter += 1
                    break

        print(f"Out of 5 countries capitals, you got {counter} right!")
        continue

    if options == "4":
        file1 = open("SearchText.txt", "r")
        filelist = file1.readlines()
        print("\nYour search history : \n")
        for line in filelist:
            print(line, end="")
        file1.close()
        continue

    if options == "5":
        name = input("\nEnter a country : ")
        response = requests.get(f"https://restcountries.com/v3.1/name/{name}")
        response1 = response.json()
        if response.status_code == 404:
            print("\nThe country you have entered does not exist!")
        if response.status_code == 200:
            test = response1[0]
            hcf = test.keys()
            if "borders" in hcf:
                a = response1[0]["borders"]
                b = []
                for item in a:
                    response2 = requests.get(f"https://restcountries.com/v3.1/alpha/{item}?fields=name")
                    response3 = response2.json()
                    b.append(response3["name"]["common"])
                print(f"\nThe country you have entered ({response1[0]['name']['common']}) borders {len(b)} countries. These are : \n")
                for item in b:
                    print(item)
            else:
                print("\nThe country you have entered does not border any other countries.")
        continue

    if options.lower() == "exit":
        break

    else:
        print("\nError! Try again.")