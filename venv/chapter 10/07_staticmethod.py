class Employee:
    company="Google"
    def getSalary(self):
        print(f"salary is {self.salary}")


    @staticmethod    
    def greet():
      print("good morning here")
    


harry=Employee()
harry.salary=10000
harry.getSalary()  
harry.greet()

 # harry.getSalary() =  Employee.getSalary(harry)  
 #