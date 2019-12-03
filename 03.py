with open("03.txt") as f:q=f.read()[:-1].split('\n')
d = {'R':1,'L':-1,'D':-1j,'U':1j}#using 2d complex plane

s = {}
m1,m2 = 10000000,10000000#big number
p,c=0,0#p is position, c is number of steps
for j in q[0].split(','):
    for n in range(int(j[1:])):
        p+=d[j[0]]
        c+=1
        if not p in s:s[p]=c

p,c=0,0
for j in q[1].split(','):
    for n in range(int(j[1:])):
        p+=d[j[0]]
        c+=1
        if p in s:m1,m2=min(m1,abs(p.real)+abs(p.imag)),min(m2,s[p]+c)
print(int(m1))
print(m2)
