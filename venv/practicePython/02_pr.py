#part 1 write code to calculate the factorial of given number
# part 2  find the number of trailing zeros in that factorial
# 5!=5!*4!................

# num=int(input("enter to number to find factorial of it "))
# sum=1
# for i in range (1,num+1):
#     sum=i*sum

# print(sum)

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number * factorial(number-1)

def factorialTrailingZero(number):
    fact= factorial(number)
    count=0
    print(fact)
    while(fact%10==0):
        cout= count +1
        number=number/10
    return count

if __name__=='__main__':
    #number=int(input("enter a number \n "))
    #fac = factorial(number)
    #print(f"the factorial is {fac} ")
    print(factorialTrailingZero(5))