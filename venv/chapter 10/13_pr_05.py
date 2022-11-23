class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"the seates available in the train are{self.seats}")
    def fareInfo(self):
        print(f"The price of the tickest  is : RS.{self.fare}")

    def bookTicket(self):
        if (self.seats>0):
            print(f"the ticket has been booked Your seat number is{self.seats} ")
            self.seats=self.seats-1
        else:
            print("sorry the train is full")
    
    def cancleTicket(self):
        pass




intercity=Train("intercity Express:1200",90,2) 
intercity.getStatus()
intercity.bookTicket()

intercity.bookTicket()

intercity.bookTicket()
# intercity.getStatus()
# intercity.fareInfo()


