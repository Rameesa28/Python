import csv
with open('employee.csv',newline='')as csvfile1:
    data=csv.DictReader(csvfile1)
    print("---")
    for i in data:
        print(i['NAME'])
