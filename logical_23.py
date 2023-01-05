#  For example, if we give 9119 the function should return 2345, as the square is 251694(reverse the num)



n=int(input("enter the num"))
i=0
while i<=n:
    r=n%10
    k=r**2
    n=n//10
    i=i+1
    print(k,end="")
    
    
