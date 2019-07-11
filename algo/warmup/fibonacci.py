def fibList(n):
    fiblist=[-1]*(n+1)   #0 to n
    fib(n, fiblist)
    return fiblist

def fib(n, fiblist):
    if n==0 or n==1: 
        fiblist[0] = 0
        fiblist[1] = 1
    else:   
        if fiblist[n] == -1: 
            fiblist[n] = fib(n-1, fiblist) + fib(n-2, fiblist)
    return fiblist[n]

print(fibList(10))
print(fibList(20))
    