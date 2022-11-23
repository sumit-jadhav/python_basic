class Employee:
    company="Google"
    salary=100

harry=Employee()
rajni=Employee()
harry.salary=300
#rajni.salary=400

print(harry.company)
print(rajni.company)
Employee.company="YouTube"
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)

#bellow line throws an error as ,,address is not instance attribute as well as Class attribute 
#print(rajni.address)
