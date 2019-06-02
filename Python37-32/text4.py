k = open('d:/file6.txt','w')
k.writelines(" how are you are you there  what are you doing")
print("data successfully wriiten in the file")
k.close()
k = open('d:/file6.txt','r')
m = k.readlines()
l = m.split()
n = input(" enter substring :")
count = 1
for i in l:
    if i == n:
        print(count,":",l)
        count +=1 
    else:
        count +=1
