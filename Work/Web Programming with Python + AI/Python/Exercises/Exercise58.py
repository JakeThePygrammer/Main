import requests

def JokeDictionary(category1):
    jokedict = {}

    response = requests.get("https://api.chucknorris.io/jokes/categories")
    response1 = response.json()
    for item in response1:
        response2 = requests.get(f"https://api.chucknorris.io/jokes/random?category={item}")
        jokedict[item] = response2.json()["value"]
    if category1 in jokedict.keys():
        print(f"\nJoke : {jokedict[category1]}")
    else:
        print(f"\nCategory does not exist!")


def JokeQuery(query):
    response = requests.get(f"https://api.chucknorris.io/jokes/search?query={query}")
    response1 = response.json()
    if response.status_code != 400:
        if response1["total"] > 0:
            for index in range(response1["total"]):
                print(response1["result"][index]["value"])
                if input("Would you like another joke(Y/N) : ").lower() == "y":
                    continue
                else:
                    break
        else:
            print("Oops! Nothing has been found. Please try again with a different query!")
    else:
        print("Oops! Query too short. Please try again with a different query!")

a = int(input("Would you like to search by category or by joke(1 or 2) : "))
if a == 1:
    print("Acceptable categories : ")
    response = requests.get("https://api.chucknorris.io/jokes/categories")
    response1 = response.json()
    for item in response1:
        print(item)
    b = input("Enter a category : ")
    JokeDictionary(b)
if a == 2:
    c = input("Enter search query : ")
    JokeQuery(c)
    