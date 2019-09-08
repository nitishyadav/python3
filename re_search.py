#The search() function of the re module will search through a string. It will look for any location for the specifie#d re pattern. 
#group(num): Returns an entire match
#groups(): Return all matching subgroups in tuple
#syntax: re.search(pattern,string)

import re
pattern = ['programming', 'hello']
str_line = 'Python programming is fun'
for p in pattern:
	print("searching for %s in %s" % (p,str_line))
	if re.search(p, str_line):
		print("Match Found")
	else:
		print("No match found")


