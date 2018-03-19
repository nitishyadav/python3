#Print all permutation of String
#!/usr/bin/python3
from itertools import permutations

s =input("Input a string to generate all it's permutation: ")
print("the string is: " +s)
perms = [''.join(p) for p in permutations(s)]
print(perms)