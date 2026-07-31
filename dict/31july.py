# dict : mutable  ====> key and  value  pair  ===> you can change elements of the  dict.

"""
d1={"phy":90 ,"math":78 ,"comp":89 ,"eng":78}
# key phy  value 90  , key math value 78 , key comp value 89 , key eng value 78
print(d1)
print(type(d1)) 

d2={90 : 91,"chem" :99}
print(d2)
print(type(d2))

"""
# built in function  :  len min max  sorted sum

"""
d1={"phy":90 ,"math":78 ,"comp":89 ,"eng":78}

print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))  # asc to  desc 
print(sorted(d1,reverse=True))  # desc to  asc
"""
# add in dict :

"""
d1={"phy":90 ,"math":78 ,"comp":89 ,"eng":78}
d1['bio'] =67
print(d1)
"""
# update dict : phy value 100 
"""
d1={"phy":90 ,"math":78 ,"comp":89 ,"eng":78}
d1['phy']=100
print(d1)
"""

# method :

d1={"phy":90 ,"math":78 ,"comp":89 ,"eng":78}

"""d2 =d1.copy()
d2['s.s']=56
print("original dict :",d1)
print("copy dict :",d2)

d2 =d1
d2['s.s']=56
print("original dict :",d1)
print("copy dict :",d2)
"""

"""print(d1.keys())
print(d1.values())
print(d1.items())
"""
d1={"phy":90 ,"math":78 ,"comp":89 ,"eng":78,"s.s" :71}

# print(d1.get("comp"))

# d1.pop("comp")  # key  as arg 
# print(d1)

# d1.popitem()    # last ket value remove 
# print(d1)

# fromkeys :

"""l1=["hetvi","ved","mital"]
# ans : {"hetvi":90, "ved":90, "mital":90}

d2 =dict.fromkeys(l1,90)
print(d2)
d2['hetvi'] =89
print(d2)
"""

#dict : not accessing though index and  no slicing  possible in dict. 

"""
d1={"phy":90 ,"math":78 ,"comp":89 ,"eng":78,"s.s" :71}
print(d1[0])  # not  possible 
"""

# dict  to  tuple  : 

"""
d1={"phy":90 ,"math":78 ,"comp":89 ,"eng":78,"s.s" :71}
print(tuple(d1.items()))
"""
# ex :2 

# d1={("hetvi",90),("ved",89),("mital",88)}

d1={
    "phy" :[56,78,90,91],
    "math" :[78,89,90,91],
    "comp" :[89,90,91,92],
}
print(d1)
print(d1['phy'][0])
