Fname = "Dev"
Lname = "Narayananan"
age=22


PersonalInfo = { 'Fname' : "Dev", 'Lname' :"Narayn",'age': 22}
print(PersonalInfo)
print(len(PersonalInfo))
print(len(Lname))

x=5
x**=3
print(x)


x//=3
print(x)

x=5
x&=3
print(x)

length=12
width=10

a=length*width
print(a)

print(3>=2 and 4>=1)                #and will check 
                                    #& will bitwise and


print((3>=2) & (4>=1))                #why?


print(3>=2 or 4<1) 

print(not (3>2))
# print(! (3>2))



multiline_string = '''
"String"
this is java standard
hi guys
welcome

bye guys'''

print(multiline_string)

print(Fname+' '+Lname)
print(len(Fname+' '+Lname))

print("\nhi guys\nnew line\ndon\'t dudge'jj \"book\"jjj")


#area of circle
pi=22/7
r=20
print(pi*r**2)

for i in range(0,3):
    print("i"+"="+str(i))
# print("i"+"=" i)

lengthFname=len(Fname)
for i in range(0,lengthFname):
    print(Fname[i])

# for i in range(lengthFname-1,0,-1):
#     print(Fname[i])

for i in range(-1,-lengthFname,-1):
    print(Fname[i])



newstring="\nhi guys\nnew line\ndon\'t\tdudge'jj \"book\"jjj"
print(newstring[::2])  #toprint alternate
print(newstring.count('jj'))

print(newstring.endswith('jj'))
print(newstring.endswith('jjy'))

print(newstring.expandtabs(10))


print("find of line = ",newstring.rfind("line"))

print("reverse of Fname = ", Fname[::-1])      #reverseofastring

print("\n\n")

s="hello how are you"
# x=s.index("are")
x=s.index("are",10)
print("x = ",x)


z="abc123"


print(z.isalnum())
# print(z.isnumeric())
# print(z.isalpha())
print(z.isdecimal())


s3="\u00bd"
print(s3)
print("S3 is isnumeric()? ",s3.isnumeric())
print("S3 is isdecimal()? ",s3.isdecimal())
print("S3 is digit? ",s3.isdigit(),"\n")



s4="10\u00b2"
# s4="10\u00bd"


print(s4)
print("S4 is digit? ",s4.isdigit())
print("S4 is isdecimal()? ",s4.isdecimal())
print("S4 is numeric? ",s4.isnumeric())

print("S4 is isidentifier()? ",s4.isidentifier())

s5="hi guys"
print(s5.islower())


a=["hi",'helo','how','are','you']
# print(" ".join(a))
# print("?".join(a))

s6=" ".join(a)
print(s6.strip("h"))            #strip first and last charcthers


print(s6.split("h"))            #(seperator,maxsplit)
print(s6)
print(s6.title())
print(s6.swapcase())


print("\n\n")
print(s6.replace("helo","hello"))

print(s6.startswith("hi"))
