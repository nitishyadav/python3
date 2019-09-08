#This is one of the methods of the match object.
#findall() method finds all the matches and then returns them as a list of strings
#Each element of the list represents as a match
#The method searches for the pattern without overlapping 

import re

pattern = 'Red'
colors = 'Redm Blue, Black, Red, Green'
p = re.findall(pattern, colors)
print(p)

str_line = 'Peter Piper picked a peck of pickled peppers. How many pickled peppers did Peter pick?'
pt = re.findall('pe\w+' , str_line)
pt1 = re.findall('pic\w+', str_line)
print(pt)
print(pt1)

line = 'Hello hello HELLO bye'
p = re.findall('he\w+', line, re.IGNORECASE)
print(p)



