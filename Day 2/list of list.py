def list(n):
    t=[]
    for num in range(n):
        row=[]
        for i in range(1,n):
            row.append(i)
        t.append(row)
    return t
print(list(10))        