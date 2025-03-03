import csv
korisnici = []
for i in range(3):
    name = input("Vnesi ime: ")
    last_name = input("Vnesi prezime: ")
    age = input("Vnesi godini: ")
    city = input("Vnesi grad: ")
    dictionary = {
       "name": name,
        "last_name": last_name,
        "age": age,
        "city": city
    }
    korisnici.append(dictionary)
with open("Exercise15.csv", "w", newline="") as f:
    dict_writer = csv.DictWriter(f, fieldnames=korisnici[0].keys())
    dict_writer.writeheader()
    for k in korisnici:
        dict_writer.writerow(k)
print(korisnici)
max_age = 0
najstar_korisnik = {}
with open("Exercise15.csv", "r") as f:
    dict_reader = csv.DictReader(f)
    print("Site korisnici: ")
    for line in dict_reader:
        print(line)
        if int(line["age"]) > max_age:
            max_age = int(line["age"])
            najstar_korisnik = line

print("=================")
print("Najstar korisnik: ")
for k, v in najstar_korisnik.items():
    print(f"{k} -> {v}")