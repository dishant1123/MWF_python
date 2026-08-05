# string  : immutable  sequence of characters , you can't change the value of a string

"""
s1="my name is hetvi."
print(s1)
print(type(s1))
"""
# slicing : 
"""
s1="my name is hetvi."
#   01234           
print(s1[2])
print(s1[10])
print(s1[1:5])
print(s1[:11])
print(s1[1 :])
print(s1[-1])
print(s1[1 : 12 :2])
print(s1[ :  :3])
print(s1[ :  :1])
print(s1[ -5: -2 ])
print(s1[ :  : -1 ])
"""

# task :1  using slicing  only 
"""
input : dishant dipakkumar shah
output : d.d.shah
"""
# task :2 using slicing only 
"""
ask user to  enter two string  and  interchange the  first three characters of the first string with the first three characters of the second string. 

input 1 : color   mital  ----> mit --->patal
input 2 : full    patil  ----> pat --->mitil 

output 1 : fulor 
output 2 : coll
"""
# built-in function : len min max sorted 

s1="my name is hetvi."

"""print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))
"""
# method : 

s1="mY name is hetvi."

"""print(s1.capitalize())
print(s1.lower())
print(s1.upper())
print(s1.title())
print(s1.swapcase())
print(s1.casefold())
"""

# count ,index,find,rindex,rfind:
s1="my name is the messi."

"""print(s1.count("e"))
print(s1.count("e",10,30))

print(s1.index("e"))
print(s1.index("e",10,30))
print(s1.index('is'))
print(s1.index('etvi'))

print(s1.find("e"))
print(s1.find("e",10,30))
print(s1.find('is'))
print(s1.find('etvi'))

print(s1.rindex("e"))
print(s1.rindex("i",2,20)) # 2 is start index , 18 is end index

print(s1.rfind("e"))
print(s1.rfind("i",2,20))
"""
# hw  what is  difference between  index and find  and  rindex and rfind ?? 

# spilt ,rsplit,partition,rpartition:

s1="my name is the messi."

"""print(s1.split())
print(s1.split("is"))
print(s1.split("s"))
print(s1.rsplit("is"))

print(s1.partition(" "))
print(s1.partition("is"))  # 3 part 
print(s1.partition("i"))
print(s1.rpartition("i"))
"""

# replace : 

s1="my name is the messi live in argentina."

"""print(s1.replace("messi","virat"))
print(s1.replace(" ","#"))
print(s1.replace(" ","#",1))
print(s1.replace(" ","#",2))
print(s1.replace(" ","#",3))
print(s1.replace(" ","#",4))
print(s1.replace(" ",""))
"""



