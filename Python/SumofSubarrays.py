n=int(input())
l=list(map(int,input().split()))
x=[]
x.append(l[0])
for i in range(1,n):
    x.append(x[i-1]+l[i])

y=int(input())
for o in range(y):
    a,b=map(int,input().split())
    if(a==0):
        print(x[b])
    else:
        print(x[b]-x[a-1])
        