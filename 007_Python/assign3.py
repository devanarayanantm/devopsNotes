import os

def check_directory_exist(directory,file_name):

    if os.path.exists(directory):
        file_path=os.path.join(directory,file_name)
        action=input("Enter which process to do 1 for create and 2 for delete: ")
        if action=='1':
            create_file(file_path)
        elif action=='2':
            delete_file(file_path)
    else:
        print("Directory not existd")


def create_file(file_path):
    try:
        # os.path.getsize(file_path)
        f=open(file_path,'x')
        print("file created")
        f.write("hi new file!")
        f.read(file_path)
    except:
        print("file already exists")


def delete_file(file_path):
    try:
        os.remove(file_path)
        print("file deleted")
    except:
        print("File does.t exists")

directory=input("Enter the directory: ")
file_name=input("Enter the file to create and delete: ")

check_directory_exist(directory,file_name)


  