lst = []
print(type(lst))
>>> lst.append(10)
>>> print(lst)
[10]
>>> lst
[10]
>>> lst = [20,30,40,44,50]
>>> lst
[20, 30, 40, 44, 50]
>>> lst.insert(40,4)
>>> lst
[20, 30, 40, 44, 50, 4]
>>> lst.insert(3,100)
>>> lst
[20, 30, 40, 100, 44, 50, 4]
>>> lst.remove(4)
>>> lst
[20, 30, 40, 100, 44, 50]
>>> lst.reverse()
>>> lst
[50, 44, 100, 40, 30, 20]
>>> len(lst)
6