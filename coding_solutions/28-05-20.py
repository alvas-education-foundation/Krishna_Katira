l=list()
s=list()
n=int(input())
for i in range(0,n):
 m=int(input())
 l.append(m)
 s.append(i+1)
l.sort()
if l==s:
 print("happy")
else:
 print("sad")