#  a=[1,2,3,[2,8,9,[3,4,3]]]
# o/p:[35]

a=[1,2,3,[2,8,9,[3,4,3]]]
i=0
b=[]
sum=0
num=0
count=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type (a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    count+=a[i][j][k]
                    k=k+1
            else:
                sum=sum+a[i][j]
            j=j+1
    else:
        num=num+a[i]
    i=i+1
b.append(num+sum+count)
print(b)

            