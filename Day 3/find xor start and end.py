a=int(input("enter the number"))
b=int(input("enter the number"))
xor=0
if(a>b):
    a,b=b,a
for i in range(a,b+1):
    xor+=i
print(xor)
