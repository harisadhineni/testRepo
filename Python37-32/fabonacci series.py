a = 0
b = 1
#a,b = 0,1
print(a)
print(b)
i = 1
while i <= 8:
    c = a + b
    print(c)
    # b = a
    # c = b
    # c = a
    a,b= b,c
    i = i+1
