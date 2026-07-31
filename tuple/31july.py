# tuple : immutable  ===> you can not change elements of the  tuple.

"""t1 =(1,23,45.78,True,34+8j,"ved")
print(t1)
print(type(t1))  # <class 'tuple'>

t2 = 1,23,45.78,True,34+8j,"ved" 
print(t2)
print(type(t2))  # <class 'tuple'>
"""

# built in function  :  len min max  sorted sum

"""
t1=(11,45,67,89,-90,234,56)
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))  # asc to  desc 
print(sorted(t1,reverse=True))  # desc to  asc
print(sum(t1))
"""

# update  : 

"""
t1=(11,45,67,89,-90,234,56)

t1[2] ="mital"
print(t1)  # not  changes possible in tuple  bcz of immutable
"""
# slicing :  same as  list. 

# method : 

"""t1=(11,45,67,89,-90,234,56)

print(t1.count(89))
print(t1.index(-90))
"""

# task :1 
"""
t1=(11,45,67,89,-90,234,56)
add the one  element in to tuple in last.

output  : t1=(11,45,67,89,-90,234,56,"ved")
"""

"""t1=(11,45,67,89,-90,234,56)

l1 = list(t1)
l1.append("ved")
print(tuple(l1))
""" 

# tuple in tuple :

"""t1=(("hetvi",90),("ved",89),("mital",88)) 
#      0             1          2 
# 0 ---> hetvi 90   ---> hetvi 0    90 --->1 
# 1 ---> ved 89     ---> ved  0    89 --->1
# 2 ---> mital 88   ---> mital 0    88 --->1

print(len(t1))

print(t1[2])
print(t1[1][1])
print(t1[2][-1])
"""

# tuple  in  list  : 

"""t1=(["hetvi",90],("ved",89),["mital",88])

print(t1)
print(t1[0])
print(t1[0][0])

# t1[0][1] ="raju"  # print   not given  error  bcz  we changes in list 
t1[1][0] ="raju"  # error 

print(t1)  
"""

# h ---> raju 90  ved 89  mital 88 
# v ---> hetvi raju  ved 89  mital 88
# m ---> hetvi 90 raju   ved 89  mital 88 