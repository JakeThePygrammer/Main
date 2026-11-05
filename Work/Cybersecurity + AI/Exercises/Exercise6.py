import sys

data = sys.stdin.read()

list1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list2 = ["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
answer = ""
for i in data:
    for char in i:
        if char == "\n" or char == " ":
            answer += " "
            continue
        index = list1.index(char)
        answer += list2[index]

print(answer)

