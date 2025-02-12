import re

def extract_email(filename):
    pattern=r'[a-zA-z0-9._+-]+@[\w].[a-zA-z]{2,}'
    try:
        f=open(filename)
        filecontent=f.read()
        emails = re.findall(pattern,filecontent)
        for email in emails:
            print(email)
    except:
        print("Some Exception occured")

filename=input("Enter the filename: ")
extract_email(filename)