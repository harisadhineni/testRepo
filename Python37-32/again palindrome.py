# programe to write palindrome

n = input('enter the value of n :')

rev = ''
for i in range(len(n)-1,-1,-1):
    rev = rev + n[i]
if n == rev:
    print('this is palindrome ')
else:
    print('this is not palindrome')    #  M A D A M
                                            # 0 1 2 3 4
