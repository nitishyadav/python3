#THe wrap() function is used to wrap an entire paragraph in to a single string. The output will be a list  of output lines.
#syntax:textwrap.wrap(text,width)
import textwrap
sample_string = '''Python is an interpreted high level programming language for general purpose programming. Created by guido van Rossum and first released in 1991, python has a design philosophy that emphasizes code reliability, notably using significant whitespaces'''

w = textwrap.wrap(text=sample_string, width=30)
print(w) 
