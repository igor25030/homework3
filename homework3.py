my_list = [1, 2, 3]   #1
my_new_list = [i * 2 for i in my_list]
print(my_new_list)

lst = [1,2,3]   #2
c=0
for i in lst:
    c+=i*i
print(c)

s = 'Hello world' #3
if ' ' in s:
    s=s.upper()
    print(s)
else:
    s = s.lower()
    print(s)

year1 = 2020   #4
year2 = 1900
year3 = year1 - year2
for i in range(year3+1):
    print(year2 + i)
