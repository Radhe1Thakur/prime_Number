start = int(input("Enter the starting point of prime no. :"))
end = int(input("Enter the ending point of prime no. :"))
print('\nThe prime numbers from {} to {} .'.format(start,end))
for n in range(start,end+1):
	for i in range(2,n+1):     #n+1 is used to run loop upto n
		if n != i:
			if n % i == 0:
				break
		else:
			print(n)
