# concatenate devops,batch,2

str="devops"+" batch"+" 2"
print(str)
print(len(str))


#str=str.upper()
print(str.upper().find("BATCH"))    #CASE INSENSITIVE SEARCH

# str[0]=""
print(str.split()[0])               #to print the first word

# print(str[-1:-2:-1])
print(str[-1])

# print(len(str)-1)
print(str.index(str[-1]))

# print(str.find("batch"))
print(str.index("batch"))


