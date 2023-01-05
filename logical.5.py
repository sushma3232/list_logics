a=[3,5,2,1,6,9]
i=0
b=[]
while i<=len(a)-1:
          k=str(a[i])+str(a[i+1])
          b.append(int(k))
          i=i+2
print(b)

# [35,21,69]

l=[1,3,5,2,4,6,2]
l.remove(2)
print(sum(l))
# o/p:21