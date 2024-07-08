#Printing Highest value
#print("Hi")

x = int(input("Enter 1st Number"))
y = int(input("Enter 2nd Number"))
z = int(input("Enter 3rd Number"))

if(x>y):
	if(x>z):
		print(x," is the Greatest ")
	else:
		print(z," is the Greatest ")
if(y>z):
	print(y, " is the Greatest ")
else:
	print(z, "is the Greatest ")

#But here is one drawback if we put numbers like 40,30 and 20 then it will print 40 & 30
	
