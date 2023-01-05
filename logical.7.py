# input:start=3,end=15
# output:print odd num...3,5,7,9,11,13,15

a=3
b=15
c=[]
for i in range(a,b+1):
    if i%2==0:
        pass
    else:
        print(i,end=" ")
  
  
  

l=[3,15]  
b=[]
i=l[0]
while i<=l[-1]:
    if i%2!=0:
        b.append(i)
    i=i+1
print(b)