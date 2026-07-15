import sys
x=11
d=2
while(d<x):
	if(x%d==0):
		print("given number is not a prime number")
		sys.exit()
	d=d+1
print("given number is a prime")	