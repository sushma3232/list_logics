a=[[1,2,4],[2,4,4],[1,2]]
b=[]
i=0
while i<len(a):
    sum=0
    j=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
    b.append(sum)
    i=i+1
print(b)