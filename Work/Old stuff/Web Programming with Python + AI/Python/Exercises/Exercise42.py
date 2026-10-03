def salaryperson(name, salary = 25000, increase = 10):
    print(f"The salary of the employee {name} will be increased by {salary//100*increase} dollars, and will result in their salary to be {salary+(salary//100*increase)} dollars.")

name  = input("What is the employees' name : ")
salary = int(input("What is the current employees' salary : "))
increase = int(input("How much will you increase said employees' salary : "))
salaryperson(name, salary, increase)
