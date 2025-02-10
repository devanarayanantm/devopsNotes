def square(x):
    return x**2
def cube(x):
    return x**3
def absolute(x):
    if x>=0:
        return x
    else:
        return -(x)
    
def Hof(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    else:
        return absolute
    
print(Hof('square')(10))