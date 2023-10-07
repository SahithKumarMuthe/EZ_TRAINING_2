def count_sort(l):
    s=len(l)
    count_arr=[0]*s
    result_arr=[0]*s
    for i in range(s):
        count_arr[l[i]]+=1
    for i in range(s):
        count_arr[i]+=count_arr[i-1]
    n=s-1
    while n>=0:
        result_arr[count_arr[l[n]]-1]=l[n]
        count_arr[l[n]]-=1
        n-=1
    for i in range(0,s):
        l[i]=result_arr[i]
l=list(map(int,input().split()))
count_sort(l)
for i in range(0,len(l)):
    print(l[i],end=" ")
