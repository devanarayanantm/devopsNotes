def sum_num(x):
    return sum(x)

def high_order(f,lst):
    var=f(lst)
    return var

result=high_order(sum_num,[1,2,3,4,57,5,9])
print(result)