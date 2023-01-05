a="aaaabbbccz"
b=""
count=0
chr=a[0]
for d in a:
    if d==chr:
        count+=1
    else:
        b=b+chr+str(count)
        count=1
        chr=d
b=b+chr 
print(b)