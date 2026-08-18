"""
module :random , date time , time delta ,calendar,math 

"""
import random as r 

"""print(r.random())  # 0-1  ---->  1 exclude 
print(r.randrange(1,10,2))  # 1 10  ---> 10 exclude 
print(r.randint(1,10))  # 1 10  --->  both point include

print(r.choice([1,2,3,4,"hetvi","mital","vraj"]))
print(r.choices([1,2,3,4,"hetvi","mital","vraj"],k=3))
"""

import math as m

"""print(m.factorial(5))
print(m.sqrt(25))
print(m.e)
print(m.pi)
print(m.fsum([1,2,3,4,5]))
print(m.floor(4.67))
print(m.ceil(4.01))
print(m.remainder(4,3))
print(m.pow(2,3))
print(m.lcm(4,6))
print(m.gcd(4,6))  # greatest common divisor
"""

import datetime as dt

today = dt.datetime.now()
print(today)

format_date = dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(format_date)

custom_date = dt.datetime(2022,7,18,12,30,45)
print(custom_date)
print(custom_date.day)
print(custom_date.month)
print(custom_date.year)
print(custom_date.hour)
print(custom_date.minute)
print(custom_date.second)

