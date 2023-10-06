def subset_sum(arr, n, target, current_subset=[]):
    if target == 0:
        print(current_subset)
        return
    if n == 0 and target != 0:
        return
    if arr[n - 1] > target:
        subset_sum(arr, n - 1, target, current_subset)
        return
    include_current = current_subset + [arr[n - 1]]
    subset_sum(arr, n - 1, target - arr[n - 1], include_current)
    subset_sum(arr, n - 1, target, current_subset)

arr = list(map(int, input("enter elements").split()))
target = int(input("enter target sum"))
n = len(arr)
subset_sum(arr, n, target)