Dict ={}
>>> Dict1 = dict(Dict)
>>> print(type(Dict))
<class 'dict'>
>>> Dict1 = {1:"One",2:"Two",3:"Three",4:"Four"}
>>> Dict1
{1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
>>> print(Dict1(3))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(Dict1(3))
TypeError: 'dict' object is not callable
>>> print(Dict1[3])
Three
>>> print(Dict1["Three"])
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(Dict1["Three"])
KeyError: 'Three'
>>> print(Dict1.get("Three"))
None
>>> print(Dict1.get('Three'))
None
>>> print(Dict1.keys())
dict_keys([1, 2, 3, 4])
>>> print(Dict1.values())
dict_values(['One', 'Two', 'Three', 'Four'])
>>> for i in Dict1:
	print(i)

1
2
3
4
>>> for i in Dict1:
	print(Dict1[i])

	
One
Two
Three
Four
