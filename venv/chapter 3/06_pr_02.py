letter='''\n  Dear <name> 
greeting from ABC codding house . Iam happy to tell you about your selection .

You have been selected !!!
Have a great day ahead.

thanks and regards,
SumitJadhav
Date:<date>       

'''
name=input("enter your name \n")
date=input("enter date \n ")

letter= letter.replace("<name>",name)
letter= letter.replace("<date>",date)


print(letter)