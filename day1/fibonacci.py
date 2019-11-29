#Factorial 
print("-----FACTORIAL-----")
a= int(input("Enter range lower limit : "))
b= int(input("Enter range upper limit : "))
fact=1

def factorial (number):
	if number==0:
		return 1

	if number==1:
		return number

	if number!=0:
		return number*factorial(number-1)


for i in range(a,b+1,1):
	print ("Factorial of ", i, " = ", factorial(i))