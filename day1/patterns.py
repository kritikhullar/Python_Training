#pattern 1
print("-----PATTERN 1-----")
a=int(input("enter no."))
for i in range(a+1):
    print("*"*i)

#pattern 2
print("-----PATTERN 2-----")
a=int(input("enter no."))
for i in range(a,0,-1):
    print("*"*i)

#pattern 3
print("-----PATTERN 5-----")
a=int(input("enter no."))
s=0
for i in range(a,0,-1):
    s=a-i
    print(" "*s+"*"*i)

#pattern 4
print("-----PATTERN 4-----")
a=int(input("enter no."))
for i in range(a+1):
    s=a-i
    print(" "*s+"*"*i)



#pattern 5
print("-----PATTERN 5-----")
a=int(input("enter no."))
for i in range(a+1):
    s=a-i
    print(" "*s+"* "*i)



#pattern 6
print("-----PATTERN 6-----")
string = input("Enter String: ")
lines=len(string)

i=1
spaces=(lines-1)
letter=1

while i<=lines:
    print(" "*(spaces),end="")
    spaces=spaces-1
    str=string[0:letter]
    letter=letter+1
    print(str)
    i=i+1
