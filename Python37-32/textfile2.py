#Text files

k = open('d:/file4.txt','w')
k.writelines("pyhon is a oop \n interpatetor\n and python is very easy to learn")
print("successfully writtrn in the text file ")
k.close()
k = open('d:/file4.txt','r')
print(k.read())
