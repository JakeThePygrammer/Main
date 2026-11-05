import sys


data = sys.stdin.read().split()
state = 0

if len(data[0]) >= 8:
    state += 1
    for char in data[0]:
        if char.isdigit():
            state += 1
            break

if state == 0:
    print("WEAK")
if state == 1:
    print("MEDIUM")
if state == 2:
    print("STRONG")

