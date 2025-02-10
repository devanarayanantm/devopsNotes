days=("mon",'tue','wed','thu','fri','sat','sun')

print(days[2:])

newday=tuple(["new"])    #if we have only one element it will take as string so make a list and make a tuple fron it
newday=("new",'day') 

print(type(newday))
days=days+newday
print(days)


tuplelist=list(days)
print(tuplelist)