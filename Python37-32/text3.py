k = open('d:\\file5.txt','r')
n = input('enter the sub string for search :')
count = 1
try:
    for i in k:
        if n in i:
            print(count,':',i)
            count += 1
        else:
            count += 1       # sub string "hari"
except:
    print("string is not found")
         
