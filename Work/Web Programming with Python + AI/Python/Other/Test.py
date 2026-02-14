class Class: #class definition
    def __init__(self, name, surname, phone): #constructor method
        self.name = name        #Defining variables
        self.surname = surname
        self.phone = phone
    def display(self):
        print(f"{self.name}, {self.surname}, {self.phone}")
    def changephonenumber(self, new_phone):
        self.phone = new_phone
    def greeting(self):
        print(f"Greetings {self.name} {self.surname}!")
        #Method creation
    def __str__(self):
        return f"{self.name}, {self.surname}, {self.phone}"
        #A str method is required for printing

user1 = Class("Klara", "Simonova", "070000002") #Element creation
user2 = Class("Andrea", "Simonov", "070000001")
print(user2)
user1.display()
user2.greeting() #Using methods
user1.changephonenumber("070123456")
print(user2.name)
print(user2.surname)
print(user1.phone) #You can print individual variables
print(type(user1)) #Returns class name
print(isinstance(user1,Class)) #Checks if element is in class and returns T/F