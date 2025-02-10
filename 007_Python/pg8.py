person = {'name':'devan','age':20,'uid':290398, 'friends': ['ak','bk'] , 'marks' : {'chem':[40],'maths':33}}
print(person)
print(len(person))
# print(person['marks'].get("chem"))
print(person['marks']['chem'])

person['address']='palakkad'
print(person.get('address'))
print('age' in person)


# person.pop('address')
# print('address' in person)
del person['address']
print('address' in person)


person['marks']['chem'].append(55)
print(person['marks'])

print(person.items())
person_copy=person
del person
print(person_copy)
# print(person) #show undefined

keyperson=person_copy.keys()
print(keyperson)
print(person_copy.values())


# for i in keyperson:
#     print(person_copy[i])



