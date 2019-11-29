days={
	1:"Friday",
	2:"Saturday",
	3:"Sunday",
	4:"Monday",
	5:"Tuesday",
	6:"Wednesday",
	0:"Thursday"
}

date=int(input("Enter the date in November: "))
rem = int(date% 7)
print("The day is ", days[rem])