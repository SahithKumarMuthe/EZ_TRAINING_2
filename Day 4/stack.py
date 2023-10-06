import collections as stack
l=[]
n=int(input("enter the no of elements"))
for i in range(n):
    a=int(input("enter the number"))
    l.append(a)
    
print(l)
for i in range(n):
    print(l.pop())
print(l)
