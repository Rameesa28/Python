import csv
csv_col=['ID','Name','Country']
dict_data=[{'ID':1,'Name':'Rameesa','Country':'Japan'},
           {'ID':2,'Name':'Nija','Country':'UK'},
           {'ID':3,'Name':'Fathima','Country':'Japan'},
           {'ID':4,'Name':'Rahmath','Country':'UK'},
           {'ID':5,'Name':'Nowfi','Country':'America'}]
csv_file="Names.csv"
try:
  with open(csv_file,'w')as file1:
      writer=csv.DictWriter(file1,fieldnames=csv_col)
      writer.writeheader()
      for data1 in dict_data:
          writer.writerow(data1)
except IOError:
    print("I/O error")
data1 =csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data1:
    print(row)
                
          
        
