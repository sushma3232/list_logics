# count the number of strings where the string length is 2 or more and last charecter are same for given list

l=["abc","xyx","cdc","121"]
c=0
for word in l:
    if len(word)>1 and word[0]==word[-1]:
        c=c+1
print(c)
        
        
        
# a=["abc","xyz","cdc","121"]
# i=0
# b=[]
# while i<len(a):
#     b=a[i]
#     j=0
#     while j<len(a):
#         c=b[j]
#         if c[0]==c[-1]:
#             b.append(c)
#             j=j+1
#         i=i+1
# print(b)
            
            
            
i=41
while i<=20:
    print(i-40)
    i=i+1