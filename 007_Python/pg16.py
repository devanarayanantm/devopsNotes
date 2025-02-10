# # def sum(a,b):
# #     return a+b

# # print(sum(7,9))

# mysum=lambda a,b : a+b

# # print((lambda a,b : a+b) (5,10))

# print(mysum(5,10))



def power(x):
    return lambda n: x**n

print(power(5)(2))              #here  taken by poewr 2nd arg taken by lamda