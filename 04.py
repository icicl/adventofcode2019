import re
with open("04.txt") as f:m,m2 = (int(i) for i in f.read()[:-1].split('-'))
s1,s2=0,0
for i in range(m,m2+1):s1+=(''.join(sorted(str(i)))==str(i))&any(str(i)[k]==str(i)[k+1] for k in range(5))
#for i in range(m,m2+1):
#    j = str(i)
#    if ''.join(sorted(j)) == j:s1+=any(j[k]==j[k+1] for k in range(5))
print(s1)

def test(j,t=0):
    if ''.join(sorted(j)) == j:
        l,n=0,''
        for c in range(6):
            if j[c]==n:l+=1
            else:t,l,n=(0,1)[l==2]|t,1,j[c]
        if l==2:t=1
    return t
for i in range(m,m2+1):s2+=test(str(i))
print(s2)
            
