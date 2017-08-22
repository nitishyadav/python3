#!/usr/bin/python3

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format("Hi Nitish",
"how are you.",
"it's been long",
"we need to catch up"))