import subprocess
res = subprocess.run(['ls','-l'],stdout=subprocess.PIPE,)
print('returncode:', res.returncode)
print('{} bytes in stdout:\n{}'.format(len(res.stdout), res.stdout.decode('utf-8')))
