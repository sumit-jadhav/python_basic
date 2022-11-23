#write a program ehich will keep adding a stream of number input by the user.stop ehrn pressed q 
sum=0
while(True):
    userInput=input("enter the price of intem or press 'q' to quit ")
    if(userInput != "q"):
        sum+=int(userInput)
        print(f" \n the amout till now : {sum} ")

    else:
        print(f"your bill total is {sum} ")
        print("thanks \n  caculation completed")
        break


#receipt printer