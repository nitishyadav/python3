#'getpass' module to handle passwords at runtime
#getpass() module in Python rompts user to enter password without echoing

import getpass
try:
	p = getpass.getpass()
except Exception as error :
	print('ERROR', error)
else:
	print('Password entered:', p)