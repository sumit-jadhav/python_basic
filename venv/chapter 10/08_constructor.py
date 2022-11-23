class Employee:
    company="Google"

    def __init__(self,name,salary,subinit):
        self.name=name
        self.salary=salary
        self.subinit=subinit
        print("employee is created")
    
    def getDetails(self):
        print(f"the name of the employee is{self.name}")
        print(f"the name of the employee is{self.salary}")
        print(f"the name of the employee is{self.subinit}")


    @staticmethod    
    def greet():
      print("good morning here")
    
harry=Employee("harry",1000,"facebook")
harry.getDetails()

# harry=Employee()
# harry.salary=10000
# harry.getSalary()  
# harry.greet()
