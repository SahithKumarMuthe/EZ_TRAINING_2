def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a number:"))  
if (n<0):
    print("factorial is not defined for negative numbers")
else:
    print("the factorial is:",fact(n))
