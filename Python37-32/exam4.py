# palindrome 

a = input('enter value a:')
k = list(a)
g = list(reversed(a))

if k == g:
    print ('this is a palindrome')
else:
    print('not a palindrome')
