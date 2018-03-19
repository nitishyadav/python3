#Replace the specific string

#!/usr/bin/python3

import re
#s = input("enter a string: ")
b =list(input("enter a string: "))

#print(s)
print(b)
a=input("input the character which you want to delete: ")

for char in b:
    if(char ==a):
        b.remove(char)
    else:
        pass
print(b)
