
a=["one","two","three"]
i=0
while i<len(a):
    print(i+1,":",a[i])
    i=i+1
    
    
# output-
# 1:one
# 2:two
# 3:three


a="my name is indhu"
b=a.split()
print(b)
i=0
c=" "
d=[]
while i<len(b):
    c=c+b[i]+"_"
    i=i+1
print(c)

    
    
# d={"a":[2,3,4,5],"b":[4,8,7,3],"c":[9,6,5,8]}
# for i in d
#     g=d[i]
#     # print(g)  
#     l=[]
#     sum=0
#     j=0
#     while j<len(g):
#         sum=sum+d[i][j]
#         j=j+1
#     l.append(sum)
#     d[i]=l
# print(d)