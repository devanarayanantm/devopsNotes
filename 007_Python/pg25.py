import os

def list_all_directory(directory):
    try:
        if os.path.exists(directory):
            for file in os.listdir(directory):
                filepath=os.path.join(directory,file)
                if os.path.isfile(filepath):
                    print("File name: ",file,"Size of file: ",os.path.getsize(filepath))
    except:
        print("Directory doesn't exists")


directory=input("Enter the directory name: ")
list_all_directory(directory)