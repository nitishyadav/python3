#The sub() is used for replacing the re pattern with the specified replacement.
#It will replace all the occurences of the pattern with the replacement string
#syntax: re.sub(pattern, repl_string, count=0)
#For sount the default value is 0 meaning replace all occurences


import re
str_line = 'Peter Piper picked a peck of pickled peppers. How many pickled peppers did Peter Piper pick?'

print("Original: ", str_line)
p = re.sub('Peter', 'Mary', str_line)
print("Replaced: ", p)


p = re.sub('Peter', 'Mary', str_line, count=1)
print("Replacing only one occurence of Peter...")
print("Replaced: ", p)


