a=[1,2,3,4]
b=[4,5,6,2]
c=[]
i=0
while i<len(a):
    d=a[i]*b[i]
    c.append(d)
    i=i+1
print(c)

# o/p[4,10,18,8]