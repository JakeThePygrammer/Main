import sys

data = sys.stdin.read().split()
if data[0] == "admin" and (data[1] == "READ" or data[1] == "WRITE" or data[1] == "DELETE"):
    print("ALLOWED")
elif data[0] == "editor" and (data[1] == "READ" or data[1] == "WRITE"):
    print("ALLOWED")
elif data[0] == "viewer" and (data[1] == "READ"):
    print("ALLOWED")
else:
    print("DENIED")
