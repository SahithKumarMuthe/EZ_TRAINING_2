def linear_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1  
    for i in range(n):
        if arr[i] == target:
            return i  
    return -1
arr=list(map(int,input().split()))
target=int(input())
result = linear_search(arr,target)
if result != -1:
    #print(f"{target} found at index {result}")
    print(target,"found ant index",result)
else:
    #print(f"{target} not found in the list")
    print(target,"not found index",result)
