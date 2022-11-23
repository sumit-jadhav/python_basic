comment=input("enter the text comment")
spam=False

if("make a lot of money" in comment):
    spam=True
elif("buy now"in comment):
    spam=True
    
elif("click these"in comment):
    spam=True
elif("subscribe this "in comment):
    spam=True

if(spam):
    print("these text is spam")
else:
    print("thse text is not spam")