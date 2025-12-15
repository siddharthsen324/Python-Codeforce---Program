t=int(input())
for _ in range(t): 
    n=int(input())
    ones=0
    temp=n
    while temp>0:
        if temp%2==1:
            ones+=1
        temp//=2
    ans=0
    for i in range(ones):
        ans=ans*2+1
    print(ans)           