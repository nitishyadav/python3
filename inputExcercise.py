#!/usr/bin/python3
age = input("How old are you?")
height=int(input("What is your height in cm:"))
#agrv means agrument vector, from sys import import argv feature
from sys import argv

#these following line help to get the command line argument
script,first,second,third =argv

print("The script is called:",script)
print("Your first cmd arg variable is:",first)
print("Your second cmd arg variable is:",second)
print("Your third cmd arg variable is:",third)
