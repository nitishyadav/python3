#The match() function is a function of the re module.This function will match the specified re pattern with the string. 
#if the match is found, a match object is returned. 
#group(num): returns an entire match
#groups(): Return all matching subgroups in tuple
#syntax: re.match(pattern,match)
import re

str_line = "This is for gathering and distributing information. Do you enjoy learning ?"
obj = re.match(r'(.*) enjoy (.*?) .*', str_line)
if obj:
	print(obj.groups())



