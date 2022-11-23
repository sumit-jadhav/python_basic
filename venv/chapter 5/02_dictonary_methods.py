myDict={
    "Fast":"In a quick manner ",
    "Harry":"A Coder",
    "Marks":[1,2,5],
    "anotherdict":{'sumit':'player'},
    1:2
}
#dictonary methods

# print(type(myDict.keys()))
# print(list(myDict.keys()))
# print(myDict.values())#to prit the values
# print(myDict.keys())#to print the keys
print(myDict.items())#print all the items in the dicto. (key,value)
print(myDict)
updateDict={
            "sumit":"friend",
            "lovish":"friend",
            "Harry":"Dancer"
    }
myDict.update(updateDict)#update the dict by adding key value pairs from updateDict
print(myDict)


print(myDict.get("Harry2"))#returns none as harry2 is not present in the dictonary
#print(myDict["Harry2"])#throws an error as harry2 is not present in the dictonary