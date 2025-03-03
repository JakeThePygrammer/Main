class Student:
    def __init__(self, __name, __surname, __phone_number):
        self.__name = __name
        self.__surname = __surname
        self.__phone_number = __phone_number
    def __str__(self):
        return f"Name : {self.__name}, Surname : {self.__surname}, Phone number : {self.__phone_number}."
    @staticmethod
    def get_mobile_operator(mobile_number):
        if len(mobile_number) == 9 or len(mobile_number) == 13:
            if mobile_number[:3] == "077" or mobile_number[:3] == "076":
                return "A1"
            elif mobile_number[:3] == "070" or mobile_number[:3] == "071":
                return "Telekom"
            elif mobile_number[:3] == "079":
                return "Lycamobile"
            else:
                return "Unknown mobile operator"
        else:
            print("Enter a number in the format +38907XXXXXXX or 07XXXXXXX")
    def getname(self):
        return self.__name
    def getsurname(self):
        return self.__surname
    def getphonenumber(self):
        return self.__phone_number
    def getall(self):
        return self.__name,self.__surname,self.__phone_number
    def changename(self,newname):
        self.__name = newname
    def changesurname(self,newsurname):
        self.__surname = newsurname
    def changephonenumber(self,newnumber):
        if len(newnumber) == 9 or len(newnumber) == 13:
            self.__phone_number = newnumber
        else:
            print("Enter a number in the format +38907XXXXXXX or 07XXXXXXX")
    def changeall(self,newname,newsurname,newnumber):
        self.__name = newname
        self.__surname = newsurname
        if len(newnumber) == 9 or len(newnumber) == 13:
            self.__phone_number = newnumber
        else:
            print("Enter a number in the format +38907XXXXXXX or 07XXXXXXX")
        print("Changing...")
s1 = Student("Jake", "Nestor", "070316555")
s2 = Student("Ana", "Colland", "076343215")
s3 = Student("Petar", "Jamesons", "077555697")

print(s1.getname())
print(s2.getsurname())
print(s3.getphonenumber())
print(s3.get_mobile_operator(s3.getphonenumber()))
print(s1.getall())
print(s1.get_mobile_operator(s1.getphonenumber()))
s1.changeall("Miso", "Dexter", "076555852")
print(s1.getall())
print(s1.get_mobile_operator(s1.getphonenumber()))


