>>> set1={}
>>> print(type(set1))
<class 'dict'>
>>> set1 = set({})
>>> print(type(set1))
<class 'set'>
>>> set1 = {10,20,10,20,30,40}
>>> set1
{40, 10, 20, 30}
>>> set2=set({30,40,50,60,70})
>>> set2
{50, 70, 40, 60, 30}
>>> set1-set2
{10, 20}
>>> set2-set1
{50, 60, 70}
>>> set1.union(set2)
{70, 40, 10, 50, 20, 60, 30}
>>> set2.union(set1)
{70, 40, 10, 50, 20, 60, 30}
>>> set1.intersection(set2)
{40, 30}
>>> set2.intersection(set1)
{40, 30}