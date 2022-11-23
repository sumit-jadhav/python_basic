myDict={
    "panka":"Fan",
    "daba":"Box",
   "Vastu":"Item"

}
print("Options are ",myDict.keys())
# print("Options are ",myDict.values())

a=input("enter the hindi word \n")

#bellow line will not throw the error  because of the get()  fuction used
print("The mening of the word is :",myDict.get(a))


