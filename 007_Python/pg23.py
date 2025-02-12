import os

cwd = os.getcwd()
print(cwd)
try:
    f=open("test1.txt","a")
    f.write("\nhii\nnewline\nbye")   
    f.close()
    f=open("test1.txt","r")
    # print(f.read())
    print(f.readlines())
    #before deleting you need to create a file before 
    # os.remove("c:\Users\Administrator\devops\git\test.txt")

except:
    print("File_error")
finally:
    f.close()