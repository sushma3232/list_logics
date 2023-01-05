l="MahEsH"
i=1
b=[]
c=[]
while i<len(l):
    if l[i].islower():
        b.append(l[i])
    else:
        c.append(l[i])
    i=i+1
print(b)
print(c)




l="MahEsH"
i=0
b=[]
c=[]
while i<len(l):
    if l[i].isupper():
        b.append(i)
    else:
        c.append(i)
    i=i+1
print(b)
print(c)





l="ManJuShA"
i=1
b=[]
while i<len(l):
    if l[i].islower():
        print(l[i],end=",")
    i=i+1


        
# o/p:5   
L=[1,2,2,5,8,4,4,8]
a=[ ]
i=0
while i<len(L):
	if L[i] not in a:
		a.append(L[i])
	i=i+1
print(len(a))
