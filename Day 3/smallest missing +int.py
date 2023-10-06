a=input()
b=[int(x) for x in a.split()]
for i in range(0,len(b)):
    if i not in b:
        print(i)
        break