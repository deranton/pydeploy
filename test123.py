import os, sys

def checkStatus(statusCode):
    if statusCode != 0:
        sys.exit(1)

print("Testing...")
print(os.system("dir /a"))
