email = input("Enter your email address: ")
partsofmail = email.split("@")
name = partsofmail[0].split(".")
print(f"The name is {name[0].capitalize()} and the surname is {name[1].capitalize()}, with initials {name[0][0].capitalize()}{name[1][0].capitalize()}.")