rechnik = {"ime_na_kurs" : "Napreden Phyton", "br_shlushateli" : 13, "lokacija": "Semos edukacija", "mesto" : "Semos Edukacija"}
print(rechnik.keys())
print(rechnik.values())
for key in rechnik.keys():
    print(f"Key {key}")
    print(f"Second letter of key {key[1]}")
for value in rechnik.values():
    print(f"Value {value}")
    if type(value) == str and len(value) > 3:
        print(f"Third letter of key {value[3]}")
    else:
        print("This value is not a word, or is shorter that than 3 letters")
for item in rechnik.items():
    print(f"Pair of key and value {item}")
