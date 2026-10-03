def agefunction(yob):
    return 2025 - yob
a = int(input("Enter your year of birth : "))
print(f"You are {agefunction(a)} years old.")