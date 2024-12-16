import csv

a = 0
b = input("Enter the name of your file: ")

if not b[-4:] == ".csv":
    print("Your file is not a .csv file")
else:
    try:
        with open(b, "r") as f:
            dict_reader = csv.DictReader(f)
            for line in dict_reader:
                a += 1
        c = int(input("Enter how many rows of the file would you like to print: "))

        if c > a:
            print("Your number is too large. There are not enough rows. Printing all rows.")
            c = a

        with open(b, "r") as f:
            dict_reader = csv.DictReader(f)
            row_count = 0
            for line in dict_reader:
                if row_count < c:
                    print(line)
                    row_count += 1

    except FileNotFoundError:
        print("File not found, please add an existing file.")
    except ValueError:
        print("Please enter a valid number of rows to print.")


