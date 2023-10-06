def fib(n):
    fib1=[]
    a,b=0,1
    while len(fib1)<n:
        fib1.append(a)
        a,b=b,a+b
    return fib1
n=int(input("enter number:"))
res=fib(n)
print("fib_series is:",res)