lst=[10,20,30,40,50,60]
lst2=[]

for x in lst:
	if x>30:
		lst2.append(x)
print(lst2)

#list comprehention
lst3 = [y for y in lst if(y>20)]
print(lst3)