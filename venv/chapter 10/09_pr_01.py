class Programmer:
    company = "microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getDetails(self):
        print(
            f"The name of the {self.company} Employee is {self.name} and the product is {self.product}")


harry = Programmer("harry", "shypnet")
Alka = Programmer("Alka", "github")
harry.getDetails()
Alka.getDetails()
