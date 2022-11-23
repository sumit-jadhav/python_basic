# n=0
# product=1
# for i in range(n):
#     product=product*(i+1)
# print(product)

def factorial_iter(n):
   product=1
   for i in range(n):
      product=product*(i+1)
   return product
def fact_recu(n):
   if n==0 or n==1:
      return 1
   
f=factorial_iter(5)
print(f)