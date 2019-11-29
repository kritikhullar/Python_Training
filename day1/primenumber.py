num = int(input("Enter a number: "))
#to check whether number is prime or not
i = 2
flag = 0
while i< num:
	 if num%i == 0:
	 	flag=1
	 	break
	 else:
	 	i+=1

if flag == 0:
	print(str(num)+" is a prime number")
else:
	print(str(num)+" is not a prime number")