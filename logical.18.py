# s = "i like this program very much"
# words = s.split(' ')
# string = []
# for word in words:
#     string.insert(0, word)
# print(" ".join(string))



a="sky is blue"
b=a.split()
c=" "
i=0
while i<len(b):
    b.reverse()
    c=c+""+b[i]
    i=i+1
print(c)
# o/p:blue is sky