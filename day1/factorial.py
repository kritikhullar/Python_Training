#Fibonacci 
print("-----FIBONACCI-----")
a= int(input("Enter no of terms : "))

def fibonacci (num):
	if num<=1:
		return num
	else:
		return (fibonacci(num-1)+fibonacci(num-2)) 
if a<=0:
	print("Enter positive")
else:
	for i in range(a):
		print (fibonacci(i), end = "\t")
