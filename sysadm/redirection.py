#accepting input by redirection
#we use stdin.pipe - this concept means providing the output of one program as the input to another program
import sys
class Redirection(object):
	def __init__(self, in_obj, out_obj):
		self.input = in_obj
		self.output = out_obj
	def read_line(self):
		res = self.input.readline()
		self.output.write(res)
		return res

if __name__ == '__main__':
	if not sys.stdin.isatty():
		sys.stsdin = Redirection(in_obj=sys.stdin, out_obj=sys.stdout)

	a = input('Enter a atring:')
	b= input('Enter another string:')

	print('Entyered strings are: ',repr(a),'and',repr(b))