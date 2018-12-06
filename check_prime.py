num = int(input('Enter The Number to Check prime no:'))
for n in range(2,num+1):
	if num != n:
		if num % n == 0:
			print('{} is not a Prime Number!!!!!!'.format(num))
			break
	else :
		 print('{} is a Prime Number!!!!!!'.format(num))
