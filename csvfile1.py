import csv
with open('emp.csv',newline='')as file1:
    data=csv.DictReader(file1)
    print("empnoempname")
    print("------------")
    for i in data:
        print(i['empno'],i['empname'])
