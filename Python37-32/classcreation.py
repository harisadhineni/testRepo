# even odd values 

list_name = [1,2,3,4,5,6,7,8]
m = filter (lambda x : x%2 == 0,list_name)
a = list(m)
print(a)
n = filter (lambda x : x%2 != 0, list_name)
b = list(n)
print(b)
