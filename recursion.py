# # # num=int(input("Enter any number:"))
# # # fact=1
# # # for i in range(num):
# # #     fact=fact*(i+1)
# # # print(fact)
# # def facto(n):
# #     product=1
# #     for i in range(n):
# #         product=product*1
# #         return product
# # def factorial_recursive(n) :   
# #     if n==1 or n==0:    
# #     return n*factorial_recursive(n-1)
# # f=facto(5)
# # print(f)
# def maximum(a,b,c):
#     if(a>b):
#         if(a>c):
#             return a
#         else:
#             return c
#     else:
#         if(b>c):
#             return b
#         else:
#              return c   
# m=maximum(2,3,4)
# print("the maximum is :"+str(m))

def farh(cel):
    return(cel*(9/5))+32
c=37
f=farh(c)
print("Fareih temperature is"+str(f)) 

print("Hello", end="")