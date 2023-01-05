

a=[-2,5,6,-7,-8]
i=0
c=""
k=""
s=","
while i<len(a):
	if a[i]>0:
	   c+=str(a[i])+s
	  
	else:
		k+=str(a[i])+s
	
	i=i+1
print("positive:",c)
print("negative:",k)    