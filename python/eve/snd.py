import time

tim = int(time.ctime()[11]+time.ctime()[12])

if tim <= 12 and tim >= 4:
    print("good morning")
if tim < 18 and tim > 12:
    print("good evening")
else:
    print("have a good night sir")