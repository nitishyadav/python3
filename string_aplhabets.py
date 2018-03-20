#Replace the specific string

#!/usr/bin/python3
#print alphabets which are not present in the string
import re
import string

s= "Hello to this world of humans"
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'
,'u','v','w','x','y','z']



not_found=set(string.ascii_lowercase) - set(''.join(s.split()))

print(not_found)


# another method
a = "Hello there what do you want"

letters=[]

for l in a:
    if(l in alpha) and (l not in letters):
        letters.append(l)
print(letters)


