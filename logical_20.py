a=[1,2,3,8,9,7]
b=[1,2,3,8,5,6]
d=[]
i=0
while i<len(a):
    if a[i] not in d:
        d.append(a[i])
    if b[i] not in d:
        d.append(b[i])
    i=i+1
print(d)
# output:[1,2,3,5,6,7,8,9]


# a=[1,2,3,8,9,7]
# b=[12,3,8,5,6]
# i=0
# d=[ ]
# a.extend(b)
# while i<len(a):
# 		if a[i] not in d:
# 			d.append(a[i])
# 		i=i+1
# print(d)