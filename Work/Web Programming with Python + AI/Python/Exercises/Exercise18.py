name = input("Enter student name: ")
surname = input("Enter student surname: ")
gradeaverage = float(input("Enter average grade: "))
initials = name[0] + surname[0]
studentdict = {"Name":name.capitalize(),"Surname":surname.capitalize(),"Grade Average":gradeaverage, "Initials" :initials.upper()}
print(studentdict)