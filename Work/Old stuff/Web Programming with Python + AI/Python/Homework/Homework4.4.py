import random

user1 = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
user2 = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]

tally1 = 0
tally2 = 0

for index in range(len(user1)):
    tally1 += user1[index]
    tally2 += user2[index]

print(f"User1 got {tally1} points!")
print(f"User2 got {tally2} points!")

if tally1 > tally2:
    print(f"User1 has won by {tally1 - tally2} points!")
elif tally2 > tally1:
    print(f"User1 has won by {tally2 - tally1} points!")
else:
    print("The points are equal!")

