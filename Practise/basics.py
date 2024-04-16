#name = "Vandan"
#print(len(name))
#print(name.find("d"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("a"))
#print(name.replace("n","o"))
#print(name*3)
#-------------------------------------------------------------
#x=1 #int
#y=2.0 #float
#z="3" #str

#x=str(x)
#y=str(y)
#z=str(z)

#print(x)
#print(y) #print(int(y))
#print(z*5)
#-------------------------------------------------------------
#name = input("Enter your name :")
#age = int(input("Enter age :"))
#height = float(input("Enter your height(in cms) :"))

#print("Hello " + name)
#print(name + ", you're "+ str(age) + " years old!")
#print("Also you're " + str(height) + "cm tall.")
#-------------------------------------------------------------
#import math
#pi = 3.14
#x=1
#y=2
#z=3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))
#print(max(x,y,z))
#print(min(x,y,z))
#-------------------------------------------------------------
#slice = [start:stop:step]
#name = "Thakar"
#fname = name[:3]
#lname = name[3:]
#funkyname = name[::2]
#revname = name[::-1]
#print(fname)
#print(lname)
#print(funkyname)
#print(revname)

#website1 = "https://google.com"
#website2 = "https://wikipedia.com"
#slice = slice(8,-4)
#print(website1[slice])
#print(website2[slice])
#------------------------------------------------------------
#age = int(input("Enter age :"))
#if age == 100:
#    print("You are a century old!")
#elif age >= 18:
#    print("You are an adult")
#elif age < 0:
#    print("You are not born yet!")
#else:
#    print("You are child")
#------------------------------------------------------------
#temp = int(input("Enter outside temperature :"))
#if temp >=10 and temp <=30:
#    print("The temperature outside is good today!")
#    print("go outside")
#elif temp <10 or temp >30:
#    print("The temperature outside is bad today!")
#    print("stay inside")

#OR
#temp = int(input("Enter outside temperature :"))
#if not (temp >=10 and temp <=30):
#    print("The temperature outside is bad today!")
#    print("stay inside")
#elif not (temp <10 or temp >30):
#    print("The temperature outside is good today!")
#    print("go outside")
#------------------------------------------------------------
#name = "" #name = None
#while len(name) == 0: #while not name:
#    name = input("Enter your name :")
#print("Hello "+name)
#------------------------------------------------------------
#import time
#for i in range(10):
#    print(i+1)

#for i in range(50,101,2):
#    print(i)

#for i in "Vandan":
#    print(i)

#for seconds in range(10,0,-1):
#    print(seconds)
#    time.sleep(1)
#print("Happy Birthday!")
#------------------------------------------------------------
#rows = int(input("Enter number of rows :"))
#columns = int(input("Enter no. of columns :"))
#symbol = input("Enter a symbol to use :")

#for i in range(rows):
#    for j in range(columns):
#        print(symbol,end="")
#    print()
#------------------------------------------------------------
#while True:
#    name = input("Enter name :")
#    if name != "":
#        break

#phone_number = "76780-03930"

#for i in phone_number:
#    if i == "-":
#        continue
#    print(i,end="")

#for i in range(1,21):
#    if i == 13:
#        pass
#    else:
#        print(i)
#------------------------------------------------------------
# print("Vandan Thakar , C168")
# food = ["pizza","burger","hotdog","sandwich"]
# print("list = "+str(food))
# print("item at index 2 = "+food[2])
# food[0] = "spaghetti"
# print("item at index 0 (pizza) replaced by spaghetti = "+str(food))
# print("all items listed down :")
# for x in food:
#    print(x)
# food.append("ice-cream")
# print("appended ice-cream = "+str(food))
# food.remove("hotdog")
# print("removed hotdog = "+str(food))
# food.insert(3,"cake")
# print("inserted cake = "+str(food))
# food.pop()
# print("popped out last item = "+str(food))
# food.sort()
# print("sorted list = "+str(food))
# print("now clearing list :)")
# food.clear()
#------------------------------------------------------------
#drinks = ["soda","tea","coffee"]
#dinner = ["pav-bhaji","pani-puri","sev-puri"]
#desert = ["cake","ice-cream"]

#food = [drinks,dinner,desert]

#print(food[1][1])
#------------------------------------------------------------
# student = ("Vandan",168,"Thakar",19)

# print("given tuple :"+str(student))
# print("counting number of 'Vandan' in given tuple")
# print(student.count("Vandan"))
# print("printing index of 19 :")
# print(student.index(19))
# print("listing down elements : ")
# for x in student:
#    print(x)
# print("checking if given element is present in the tuple or not and if not printing 'wrong info.' :")
# if "Thakar" in student:
#    print("Surname available!")
# if "Boy" in student:
#    print("Boy is here!")
# else:
#    print("Wrong information!")
#------------------------------------------------------------
# utensils = {"fork","spoon","knife"}
# dishes = {"bowl","plate","cup","knife"}
# print("Given set of utensils : "+str(utensils))
# print("Given set of dishes : "+str(dishes))
# utensils.add("butterknife")
# print("adding element in set utensils :"+str(utensils))
# utensils.remove("fork")
# print("removing element in set utensils :"+str(utensils))
# print("updated utensils set :")
# dishes.update(utensils)
# print(str(utensils))
# dinner_table = utensils.union(dishes)
# print("combining both set :"+str(dinner_table))
# print("taking out common elements from both the set :")
# print(dishes.intersection(utensils))
# print(utensils.difference(dishes))
# print("listing down elements of dinner_table set :")
# for x in dinner_table:
#    print(x)
#------------------------------------------------------------
# capitals = {'USA':'Washington DC','India':'New Delhi','China':'Beijing'}
# print("Given dictionary :"+str(capitals))
# print("adding element")
# capitals.update({'Germany':'Berlin'})
# print("updating value of key USA :")
# capitals.update({'USA':'Las Vegas'})
# print("popping china key :")
# capitals.pop('China')
# print("printing elements of dict :"+str(capitals))
# print(capitals['Germany'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key,value in capitals.items():
#    print(key,value)
#------------------------------------------------------------
#name = "vandan thAkar!"

#if(name[0].islower()):
#    name = name.capitalize()
#print(name)
#fname = name[:6].upper()
#lname = name[7:].lower()
#last_character = name[-1]

#print(fname)
#print(lname)
#print(last_character)
#------------------------------------------------------------