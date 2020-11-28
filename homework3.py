# 1-е задание
myList = [1, 2, 3]
myNewList = [i * 2 for i in myList]
print(myNewList)

# 2-е задание
myList = [1, 2, 3]
myNewList = [i * * 2 for i in myList]
print(myNewList)

# 3-е задание
s = 'Hello world' #3
if '' in s:
    s=s.upper()
    print(s)
else:
    s = s.lower()
    print(s)

# 4-е задание
from datetime import datetime

year1 = 2020
year2 = 1900
rad = year1 - year2
for i in range(rad+1):
 print(year2 + i)
