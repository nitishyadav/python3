#!/usr/bin/python3
from sys import argv
from os.path import exists
#user will provide the files in the command line aurgument while running the application
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file=open(from_file)
#to see what is coming in the file
print(">>>in_file=",repr(in_file))
#reading the content of to_file to indata
indata= in_file.read()

print(f"the input file is {len(indata)} bytes long")

print(f"Does the output file exist?{exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

#we are opening the to_file with 'w'
out_file = open(to_file,'w')
out_file.write(indata)

print("Alright,all done")

#finally we close both of the files
out_file.close()
in_file.close() 