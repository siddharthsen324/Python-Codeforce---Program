while True:
    m,n=map(int,input().split())
    if m<=0 or n<=0:
        break
    start=min(m,n)
    end=max(m,n)
    output=""
    total=0
    for i in range(start,end+1):
        output+=str(i)+" "
        total+=i
    p=output+f"sum ={total}"   
    print(p)

