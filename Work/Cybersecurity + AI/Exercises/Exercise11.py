import csv
with open('authentication_logs.csv', newline='') as f:
    rows = list(csv.DictReader(f))

tempid = ''
tempuser = ''
duplicateidcount = 0
duplicateusernamecount = 0
for r in rows:
    if r['reason'] == 'bad_password':
        if tempid == r['source_ip']:
            duplicateidcount += 1
            if tempuser == r['username']:
                duplicateusernamecount += 1
            else:
                duplicateusernamecount = 0
        else:
            duplicateidcount = 0
        tempid = r['source_ip']
        tempuser = r['username']
        if duplicateusernamecount > 1:
            print("\nBrute force attempt on:")
            print(str(duplicateusernamecount) + " attempts " + str(tempid) + " IP " + str(tempuser) + " username")
        elif duplicateidcount > 1:
            print("\nPassword spraying attempts by:")
            print(str(duplicateidcount) + " attempts " + str(tempid) + " IP")
