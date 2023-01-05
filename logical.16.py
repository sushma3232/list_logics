# a=[12,67,98,34]
# o/p:[1,6,9,3]
a=[12,67,98,34]
b=[]
i=0
while i<len(a):
    c=a[i]//10
    b.append(c)
    i=i+1
print(b)
 

# a=[12,67,98,34]
# o/p:[2,7,8,4]
a=[12,67,98,34]
b=[]
i=0
while i<len(a):
    r=a[i]%10
    b.append(r)
    i=i+1
print(b)
 