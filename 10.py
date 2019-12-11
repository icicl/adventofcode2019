from os.path import basename,exists,getsize
from os import getcwd
import requests
p = basename(__file__)
if not exists(p[:2]+'.txt') or getsize(p[:2]+'.txt')==0:
    with open(p[:2]+'.txt','w+') as f:
        h = {'Cookie':'session=53616c7465645f5f89848df8db284e700a704cd0fb43c600e0bc285403236f357d4de9730a7a0eeba46ae4541e9a2f4f'}
        url = 'https://adventofcode.com/'+getcwd()[-4:]+'/day/'+str(int(p[:2]))+'/input'
        f.write(requests.get(url,headers=h).text)
###
###
import re
with open(p[:2]+".txt") as f:
    t = f.read()[:-1]

q = t.split('\n')


m = set()
for x in range(len(q[0])):
    for y in range(len(q)):
        if q[y][x]=='#':
            m|={x+y*1j}
def gcd(x, y): 
    if y==0:return x
    while(y): 
        x, y = y, x % y 
    return x

def path(a,b):
    x,y=int(a.real-b.real),int(a.imag-b.imag)
    g=gcd(abs(x),abs(y))
    if any(int(b.real)+i*(x//g)+(int(b.imag)+i*y//g)*1j in m for i in range(1,g)):
        return 0
    return 1
mm=0
p=0
for i in m:
    n=0
    for j in m:
        if i!=j:
            n+=path(i,j)
    if n>mm:p,mm=i,n
px,py=p.real,p.imag
print(mm)
v=0
m.remove(p)
from math import atan as at
m2 = {}
p4=2*at(1)

for i in m:
    ix,iy=i.real,i.imag
    x,y=ix-px,py-iy
    if x>0 and y>0:
        m2[i]=at(x/y)
    elif x>0 and y<0:
        m2[i]=2*p4+at(x/y)
    elif x<0 and y<0:
        m2[i]=2*p4+at(x/y)
    elif x<0 and y>0:
        m2[i]=4*p4+at(x/y)
    elif x==0 and y>0:
        m2[i]=0
    elif x==0 and y<0:
        m2[i]=2*p4
    elif y==0 and x>0:
        m2[i]=p4
    elif y==0 and x<0:
        m2[i]=3*p4
#    print(i,p,x,y,m2[i])
def dist(a,b):
    return abs(a.real-b.real)+abs(a.imag-b.imag)
a=-.00000001
while v<200:
    ma=9
    d=1000
    w=0
    for i in m2:
        aa=m2[i]-a
        if aa<0:
            aa+=4*p4
        if aa==ma:
            if d>dist(i,p):
                d,w=dist(i,p),i
        elif aa<ma:
            ma=aa
            d,w=dist(i,p),i
    v+=1
#    print(v,w,a,m2[w])
    del m2[w]
    a+=max(ma+.000001,.000001)
    if a>4*p4:a-=4*p4
print(int(w.real)*100+int(w.imag))
