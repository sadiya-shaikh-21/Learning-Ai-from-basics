#For avoiding printing Greater number more than 1 we can use elif condition or condition with && 

print("Enter 3 numbers")
x = int(input("Enter 1st number "))
y = int(input("Enter 2nd number "))
z = int(input("Enter 3rd number "))

if(x>y and x>z):
	print(x, " is greater")
elif(y>x and y>z):
	print(y, " is greater")
else:
	print(z, " is greater")
