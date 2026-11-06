import csv
countersuccess = 0
counterfail = 0
precent = 0
with open('authentication_logs.csv', newline='') as f:
    rows = list(csv.DictReader(f))
    for i in range(3):
        print(rows[i])
    for r in rows:
        if r['status'] == 'SUCCESS':
            countersuccess += 1
        if r['status'] == 'FAILED':
            counterfail += 1
    precent = counterfail / (counterfail + countersuccess) * 100
    print(f"Failure rate : {precent}%")
    a = input("Please enter the desired request type(VPN/WEB/RDP) : ")
    for r in rows:
        if r['service'] == a:
            print(r)



