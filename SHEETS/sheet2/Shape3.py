n=int(input())
for i in range(1,n+1):
    sp=n-i
    str=2*i-1
    print(" "*sp + "*"*str)
    
for i in range(n,0,-1):
    sp=n-i
    str=2*i-1
    print(" "*sp + "*"*str)