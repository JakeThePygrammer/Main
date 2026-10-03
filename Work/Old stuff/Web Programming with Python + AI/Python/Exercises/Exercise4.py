imeprezimeog = input("Enter your name and surname in lowercase with a dot in between and a dot at the end: ")
imeprezimelen = imeprezimeog.replace(".", "")
print(f"Name and surname : {imeprezimeog.replace(".", " ").strip().title()}, number of letters : {len(imeprezimelen.strip())}, number of the letter a in your name : {imeprezimelen.count("a")}")