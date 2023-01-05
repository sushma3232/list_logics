a=[1,3,2,1]
i=1
c=[]
while i<len(a):
          k=a[i]-a[0]
          c.append(k)
          i=i+1
print(c)
# [2,1,0]
# (3-1,2-1,1-1)


