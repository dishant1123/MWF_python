"""
file handing :txt  file  

1. read   :only exiting  file ---> read only  -----> txt 
2. write  :new file create + write   ----> exiting file  open ----> over write 
3. append :new file create + write   ----> exiting file  open ----> last add 

function :

1. fopen : open file  / with  open  ----> loop  
2. fclose : close file
3.f.write : write in file
4.f.read : read from file
5.f.readline : read one line from file
6.f.readlines : read all line from file store in to list
"""

# ex :1 write 

"""
with open("mital.txt","w") as f :
    f.write("my name is  mital patil.\n")
    f.write("my age is 20.\n")
    f.write("love pizza.\n")
    f.write("dream to meet narendra modi.\n")
    f.close()
"""

# ex :2 write mode exiting file  : 

"""with open("mital.txt","w") as f :
    f.write("live in ahmedabad.\n")
    f.write("study in Sahjanand College.\n")
    f.write("dream city is USA.\n")
    f.write("dream to meet virat kohli.\n")
    f.close()
"""

# ex : 3 append

"""
with open("vraj.txt","a") as f :
    f.write("my name is  vraj dave.\n")
    f.write("my age is 20.\n")
    f.write("love mexican food.\n")
    f.write("dream to meet messi.\n")
    f.close()
"""

#ex : 4 append mode exiting file
"""with open("vraj.txt","a") as f :
    f.write("team leader of hackthon event.\n")
    f.write("all the best for  your hackthon event i wish you won the  prize and distribution money to old age home people.\n")
    f.close()
"""

# ex :5 read mode : open only exiting file  ---->and read only 

"""with open("vraj.txt","r") as f :
    # context = f.read()  # all the context read
    # context = f.readline()  # only one line read
    context = f.readlines()  # all line read store in to list

    print(context)
    f.close()
"""

# ex : 6 read csv file : 

import csv

"""with open("file  handing/student.csv","r",encoding="utf-8",errors="ignore",newline="") as f :
    r=csv.reader(f)
    for i in r :
        print(i)
"""
"""with open("file  handing/student.csv","r",newline="") as f :
    # c=f.readlines()
    c=f.read()
    print(c)
"""
# ex : json  file  : 

"""with open("file  handing/student.json","r") as f :
    c=f.read()
    print(c)
""" 
"""import json
with open("file  handing/student.json","r") as f :
    c=json.load(f)
    print(c)
    
"""

# exception  handing  :

"""
try :

except :
"""

# ex :1 

"""try :
    a=int(input("enter the a value a :"))
    b=int(input("enter the a value b:"))
    print("division : ",a/b)
    
except ZeroDivisionError :
    print("areee zero thi divide na thy laa ...")
"""
    
# ex :2 
"""try :
    l1=[10,20,30,40,50]
    print(l1[2])  #IndexError
except IndexError :
    print("limit ma nakhvnu baka ...")
"""

# ex :3 
"""try :
    with open("gk.txt","r") as f :
        c=f.read()
        print(c)  #FileNotFoundError
except FileNotFoundError :
    print("baka em no thy rekha .... read mode exiting file j read thy lala.")
    
finally :
    print("successfully read file")
    
"""

# task :1 
"""
ask user to enter the string  and print vowel and  consonant in seperate line like vowel.txt and consonant.txt

input  : my name is  mital patil.

vowel.txt :aeiiaai
consonant.txt :my nm s  mtl ptl.
"""
n=input("enter the  string  :")
vowel ="aeiou"

for i in n :  # my name is  mital patil.
    if i in vowel :
        with open ("vowel.txt","a") as f :  
            f.write(i)  # ae
    else :
        with open ("consonant.txt","a") as f :
            f.write(i)  #my nm

            
            

    

