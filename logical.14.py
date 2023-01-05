# o/p:[2+1=3,1+2=3,7+3=10,5+4=9,3+5=8,1+6=7]=[3,3,1,9,8,1]

a=[2,1,7,5,3,8]
i=0
c=[]
k=1
while i<len(a):
          b=a[i]
          e=str(b+k)
          if len(e)>1:
                    f=e[0]
                    g=int(f)
                    c.append(g)
          else:
                    h=int(e)
                    c.append(h)
          i=i+1
          k=k+1
print(c)


