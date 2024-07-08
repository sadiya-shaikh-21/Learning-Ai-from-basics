# Program to implement an employess insert & display operations
# EmpDB: list
# Records of employees as tuples(EmpNo,Ename,Sal)

def insertRecords(empDB, rec):
	empDB.append(rec)
	return "1"

def displayAllEmployee(empDB):
	cnt = 1
	for rec in empDB:
		print("Employee ",cnt,"# ",rec[0]," ",rec[1]," ",rec[2])
		cnt = cnt + 1

def getEmpDetails(empDB):
	print("Provide Employee Details: ")
	empno = int(input("Empno: "))
	ename = input("Ename: ")
	sal = int(input("Salary: "))
	rec = (empno, ename, sal)
	no = insertRecords(empDB,rec)
	print(no, " record inserted...")

def viewMenu(empDB):
	cont = "y"
	while(cont == "y"):
		print("1: Insert a record \n2: Display all records \n0: To Exit")
		res = int(input("Your choice: "))
		if(res == 1):
			getEmpDetails(empDB)
		elif(res == 2):
			displayAllEmployee(empDB)
		elif(res == 0):
			cont = "n"
		else:
			print("Invalid Choice...")

#Initialize Database
empDB = []
viewMenu(empDB)

#Output:
'''1: Insert a record 
2: Display all records 
0: To Exit
Your choice: 1
Provide Employee Details: 
Empno: 1
Ename: aaa
Salary: 10000
1  record inserted...
1: Insert a record 
2: Display all records 
0: To Exit
Your choice: 2
Employee  1 #  1   aaa   10000
1: Insert a record 
2: Display all records 
0: To Exit
Your choice: 1
Provide Employee Details: 
Empno: 2
Ename: bbb
Salary: 1233
1  record inserted...
1: Insert a record 
2: Display all records 
0: To Exit
Your choice: 2
Employee  1 #  1   aaa   10000
Employee  2 #  2   bbb   1233
1: Insert a record 
2: Display all records 
0: To Exit
Your choice: 1
Provide Employee Details: 
Empno: 33
Ename: ccc
Salary: 57676
1  record inserted...
1: Insert a record 
2: Display all records 
0: To Exit
Your choice: 0'''
