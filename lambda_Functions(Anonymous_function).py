ret = lambda y:y*y*y
print(ret(5))

strList = ["This", "is", "a", "session", "of", "python"]
len(strList)

125
>>> strList = ["This", "is", "a", "session", "of", "python"]
>>> len(strList)
6
>>> strList2 = list(map(lambda s:s.upper()+"!",strList))
>>> strList2
['THIS!', 'IS!', 'A!', 'SESSION!', 'OF!', 'PYTHON!']
>>> retval = lambda x:x*2 if x<5 else x
>>> retval(5)
5
>>> retval(3)
6
>>> strList3 = list(filter(lambda s:len(s)>3,strList))
>>> strList3
['This', 'session', 'python']
>>> 