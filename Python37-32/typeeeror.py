a = [10,20,30]
for i in range(4):
    try:
        for j in range(4):
            try:
                k = a[j]/2
                print(k)
            except IndexError:
                print ("Index out of range")
                k = a[j-1]/2
                print(k)

    except:
        print('run time error')
