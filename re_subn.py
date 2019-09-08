#subn() function works the same as sub() with additional functionality.
#the subn() function will return a tuple containing the new string and the number of replacements performed.

import re
print("str1:- ")
str1 = "Sky is blue.sky is beautiful."

print("Original:", str1)
p = re.subn('beautiful', 'stunning', str1)
print("Replaced: ", p)
print()

print("str_line:- ")
str_line = 'Peter piper picked a peck of pickeled peppers, How many pickled peppers did Peter pick?'

print("Oroginal: ", str_line)
p = re.subn('Peter', 'Mary', str_line)
print('Replaced: ',p)


