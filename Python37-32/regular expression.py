import re
st = 'Harikrishna is in a class '
s = re.compile('[A-Z]+')
res = s.findall(st)
print(res)
rev = 0
for i in range (len(st)-1,-1,-1):
    rev = rev+st[i]
if st == rev:
    print('the word is a palindorme')
else:
    print('none palindrome')
    
