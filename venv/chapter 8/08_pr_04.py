def sum(b):
    if b<1:
     return b
    else:
        return b+sum(b-1)

a=sum(16)
print(a)


# def rec_fun(n):
#     if n<1 :
#         return n
#     else:
#         return n + rec_fun(n-1)
# num=16
# print(rec_fun(num))
