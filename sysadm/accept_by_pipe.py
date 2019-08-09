#input by pipe is used to pass information from one program to another
#echo -e '5\n15\n20' |python3 accept_by_pipe.py
import sys
for n in sys.stdin:
	print(int(n.strip())/2)

