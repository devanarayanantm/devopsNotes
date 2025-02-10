string="hello world"
def most_repeat_char(str):
    mydict={}
    for i in range(0,len(str)):
        if str[i] in mydict :
            mydict[str[i]]+=1
        else:
            mydict[str[i]]=1
    
    max_key=max(mydict,key=mydict.get)
    max_value=mydict[max_key]
    print("max repeat char is ",max_key,", its value: ",max_value)
    return mydict

print(most_repeat_char(string))

list=['ram','rsj','dev','guru','ram']
list2=['ram']
# list.insert(4,'jj')
print(list[-1],list[0],list[(len(list))//2],len(list))
