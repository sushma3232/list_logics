

a=[1,2,3,4,5,6]
# output=[2,6,12,20]
b=[]
i=0
while i<len(a)-1:
    c=a[i]*a[i+1]
    b.append(c)   
    i=i+1
print(b)


