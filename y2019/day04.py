#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from collections import Counter as counter

a, b = 402328, 864247

def valid1(password):
    password = str(password)
    if len(set(password)) >= len(password):
        return False
    if password != ''.join(sorted(password)):
        return False
    return True
   
def valid2(password):
    password = str(password) 
    if password != ''.join(sorted(password)):
        return False
    return any(x == 2 for x in counter(password).values())


print("\n")
print("p1:", sum(1 for x in range(a, b+1) if valid1(x)))
print("p2:", sum(1 for x in range(a, b+1) if valid2(x)))
# p2 is at least 161
