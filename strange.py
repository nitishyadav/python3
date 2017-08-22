#!/usr/bin/python3
#Here is some starnge stuff

#comes in same line
days="Mon Tue Wed Thu Fri Sat Sun"
#" put inside a string with '\'
months= "Jan\nFeb\nMar\"\nApr\nMay\nJun\nJul\nAug"

print("Here are the days:",days)
print("Here are the months:",months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

#from here we start some of the escape characters
tabby_cat = "\t I'm tabbed in."
persian_cat="I'm split\non a line"
backslash_cat="I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Finishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)