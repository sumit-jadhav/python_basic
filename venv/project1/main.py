import random
#Snake Water Gun  OR Rock Paper Scissors

def gameWin(com,you):
    #if two values are equal declare a tie 
    if comp==you:
        return None
        # check for all the posibilites when computer chose snake
    elif com =='s':
        if you=='w':
            return False
        elif you=='g':
            return True
            
    # check for all the posibilites when computer chose water
    elif com =='w':
        if you=='g':
            return False
        elif you=='s':
            return True
            
        # check for all the posibilites when computer chose gun
    elif com =='g':
        if you=='s':
            return False
        elif you=='w':
            return True




#to generate input from the user
a=print("Computer Turn: Snake(s) Water(w) Gun(g) ???")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

# to take input from the user
player=input("player Turn: Snake(s) Water(w) Gun(g) ???")

a=gameWin(comp,player)
print(f"computer have chose  {comp}")
print(f"you have chose  {player}")
if a==None:
    print("The game is tie")
elif a==False:
    print("computer has won ! ")
elif a==True:
    print("you have won !")