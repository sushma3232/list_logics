l=[6,9,7,5,8]*10
print(len(l))
# o/p:50

l=[None]*10
print(len(l))
# o/p:10




reslist=[x+y for x in ["Hello","good"]for y in ["Dear","Bye"]]
print(reslist)
# ["Hello Dear","Hello Bye","good Dear","good Bye"]



# write a python program to sum all items in alist
l=[4,5,8,9,40,45,14,17,10]
b=[]
sum=0
i=0
while i<len(l):
    sum=sum+l[i]
    b.append(sum)
    i=i+1
print(sum)