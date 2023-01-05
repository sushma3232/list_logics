# remove leading 0"s
a=["00002234","00100","1789"]
b=[]
for i in a:
    while i[0]=="0":
        i=i[1:]
    b.append(i)
print(b)
# ["2234","100","1789"]


# remove zeroes
a="111abc11"
a=a.strip("1")
print(a)
        
        
