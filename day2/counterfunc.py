def funct1():			#closure design pattern
	count=1
	def inner():
		nonlocal count 
		print(count)
		count+=1
	return inner

hello=funct1()
hello()
hello()
hello()
hi=funct1()
hello()
hello()
hi()
hi()
