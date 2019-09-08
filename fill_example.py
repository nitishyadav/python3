# The fill() function works similarly to textwrap.wrap, except it returns the data joined into a single, newline-separated string
#This function wraps the input in text and returns a single string containing the wrapped text.
#syntax: textwrap.fill(text,width)

import textwrap

sample_string = '''Python is an interpreted high-level programming language.'''
w = textwrap.fill(text = sample_string,width=50)
print(w)
s = textwrap.shorten(text = sample_string, width = 50)
print(s)



