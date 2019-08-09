import getpass
passwd = getpass.getpass(prompt='Enter your Password:')
if passwd.lower() == '#pythonworld' :
	print('Welcome!!')
else:
	print('The password entered is incorrect!!')
