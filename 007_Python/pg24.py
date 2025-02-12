import csv

with open('employee.csv') as f:
    csv_reader = csv.reader(f,delimiter=',')
    linecount=0
    print(type(csv_reader))

    for i in csv_reader:
        print(i)