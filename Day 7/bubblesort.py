def sort(li):
    m=len(li)
    count=0
    for i in range(m):
        for j in range(0,m-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
li=list(map(int,input("enter the number:").split()))
sort(li)
print(li)