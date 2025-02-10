lang="python3"
# lst=list(lang)
# print(lst)

lst1= [ i for i in lang if i!='3' ]
print(lst1)

lst2= [i*i for i in range(1,11)]
print(lst2)

lst3=[(i,i*i) for i in range(1,11)]
print(lst3)
print(type(lst3[9]))
print(lst3[2][1])


lst4=[(i) for i in range(1,11) if i%2==0]
print(lst4)

lst5=[[1,2,3],[4,5],[6,7]]
flat_list=[number for row in lst5 for number in row]
print(flat_list)