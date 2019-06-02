n = int(input('enter number: '))
temp = n
rev = 0
while (n>0):                        # comment 121
    rem = n%10                       # rem = 1
    rev = rev*10+rem                  # rev = 1
    n = n//10                          # n = 21
if (temp == rev):                      # loop is continue   
    print('The number  is a palindrome')
else:
    print('The number not a palindrome')



#loop 1 
#n =121 rem = 1 rev = 1 n =12

#loop2
#n =12 rem = 2 rev = 12 n =1

#loop 3
#n =1 rem =1 rev =121 n= 0

