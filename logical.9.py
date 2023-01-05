# replace 200 in place of 20.only update the first ocurrence of value
l=[5,10,15,20,25,50,20]
i=0
while i<len(l):
    if l[3]==20:
        l[3]=200
    i=i+1
print(l)

# o/p[5,10,15,200,25,50,20]