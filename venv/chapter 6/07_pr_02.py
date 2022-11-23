sub1=int(input("enter the first subject marks \n"))
sub2=int(input("enter the second subject marks \n"))
sub3=int(input("enter the third subject marks \n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail")

elif(sub1+sub2+sub3)/3 < 40:
    print("you are fail due to total percentage is less than 40")

else:
    print("you are pass")