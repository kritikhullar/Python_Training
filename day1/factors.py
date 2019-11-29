a=int(input("Enter a number: "))
i=1
count =0
factor = 0
while i<a:
	if a%i == 0:
		print(i," is a factor of ",a)
		factor += i
		count +=1
	i+=1
else:
	print("Sum: ",factor)
	print("number of factors: ",count)
