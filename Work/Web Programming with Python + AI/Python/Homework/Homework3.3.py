def combinedstrings(text1,text2):
    finished = text1[0] + text2[0] + text1[len(text1)//2] + text2[len(text2)//2] + text1[-1] + text2[-1]
    return finished

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
print(f"Combined strings : {combinedstrings(string1, string2)}")
