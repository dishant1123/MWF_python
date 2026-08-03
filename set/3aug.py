# set : mutable  ====> you can change  elements  of the set , store only unique elements,unordered.

"""s1={100,2,2,3,3,4,5,6,7,8,9,"ved",True,34+8j,"hetvi"}
l1=[100,2,2,3,3,4,5,6,7,8,9,"ved",True,34+8j,"hetvi"]
t1=(100,2,2,3,3,4,5,6,7,8,9,"ved",True,34+8j,"hetvi")
print("set :",s1)
print("list :",l1)
print("tuple :",t1)

print(type(s1))  # <class 'set'>
"""

# empty set :

"""s1=set()
print(s1)
print(type(s1))  # <class 'set'>
"""

# note : index and slicing not possible in set beacuse set is unordered.

# built in function  :  len min max  sorted sum

"""
s1={100,2,2,3,3,4,5,6,7,8,9,True,23}

print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))  # asc to  desc 
print(sorted(s1,reverse=True))  # desc to  asc
print(sum(s1))
"""
# method :

# s1={100,2,2,3,3,4,5,6,7,8,9,True,23}

# s1.add(340)
# print(s1)

# s2=s1.copy()
# print(s2)

# s1.clear()
# print(s1)

# s1.discard(13)  # reomve 
# print(s1)

# s1.remove(2)
# print(s1)

# s1.update({340,440,540})
# print(s1)

s1={1,2,3,4,5}
s2={4,2}
s3={1,2,3,4,5,6}

"""print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))  # s1-s2
print(s1.symmetric_difference(s2))

print(s1.intersection(s2))
print(s1.intersection_update(s2))
print(s1)

print(s1.difference(s2))
print(s1.difference_update(s2))
print(s1.symmetric_difference_update(s2))
print(s1)

print(s2.isdisjoint(s1))
print(s2.issubset(s1))
print(s3.issuperset(s1))

"""

# frozenset : immutable  ===> you can not change elements of the  frozenset.

fz =frozenset({1,2,3,4,5,4,5})
print(fz)
print(type(fz))  # <class 'frozenset'>
