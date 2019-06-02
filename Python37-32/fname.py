import os,sys
fname = input("enter file name:")
word  = input ("enter word to the search :")
k = 0
with open (fname,'r')as f:
    for line in f:
        word = line.split()
        for i in word:
            if (i == word):
                k= k+i

print("occurence of the word :")
print(k)
sys.exit(0)

