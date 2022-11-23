class Employee:
    company="Google"
    def getSalary(self):
        print(f"salary is {self.salary}")

harry=Employee()
harry.salary=10000
harry.getSalary()  

 # harry.getSalary() =  Employee.getSalary(harry)  
 #