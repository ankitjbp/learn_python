"""
step 1 - take a number
step 2 - initiate factorial with 1
step 3 - multiply that number with, 
factorial 
step 4 - reduce number by 1
step 5 - go to step 3 till we get value as 1 of our number
step 6 - print factotial
"""

number=33
factorial=1
while(number>1):
	factorial=factorial*number
	number=number+1
print(factorial)

