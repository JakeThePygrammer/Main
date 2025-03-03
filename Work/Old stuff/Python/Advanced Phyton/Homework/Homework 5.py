import csv
korisnici = []
for i in range(5):
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    email = input("Enter email: ")
    dictionary = {"name": name, "surname": surname, "email": email}
    korisnici.append(dictionary)
with open("Homework5.csv", "w", newline="") as f:
    dict_writer = csv.DictWriter(f, fieldnames=korisnici[0].keys())
    dict_writer.writeheader()
    for k in korisnici:
        dict_writer.writerow(k)
with open("Homework5.csv", "r") as f:
    dict_reader = csv.DictReader(f)
    print("All users: ")
    for line in dict_reader:
        print(f"{line['name']} {line['surname']} ---------> {line['email']}")
