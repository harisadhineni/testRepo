# csv files
import csv
k = open ('d:\\fileexcel.csv','r')
s = csv.reader(k)
print(s)
data = list(s)
for line in data:
        print(line,'\t',end='')

k.close()

