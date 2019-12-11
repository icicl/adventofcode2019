from itertools import combinations as co
from itertools import permutations as pe
import hashlib
def md5(x):
    return hashlib.md5(x.encode()).hexdigest()
###
###
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
#t="3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
t="3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
q = t.split(',')


d2=[int(i) for i in q]

def  _12(a,b,c):
    if (a//100)%10==0:b=d[b]
    if a//1000 == 0:c=d[c]
    if a%10==1:return b+c
    return b*c
def ic(in1,in2,d):
    i=0
    r=0
    while True:
        if d[i]%10 in (1,2):
            a,b,c=d[i],d[i+1],d[i+2]
            if (a//100)%10==0:b=d[b]
            if a//1000 == 0:c=d[c]
            if a%10==1:rr= b+c
            else:rr= b*c
            d[d[i+3]]=rr
            i+=4
        elif d[i]==3:
            d[d[i+1]]=in1
            in1=in2
            i+=2
        elif d[i]==4:
            r=(d[d[i+1]])
            i+=2
        elif d[i]==104:
            r=(d[i+1])
            i+=2
        elif d[i]==5:
            if d[d[i+1]]!=0:i=d[d[i+2]]
            else:i+=3
        elif d[i]==105:
            if d[i+1]!=0:i=d[d[i+2]]
            else:i+=3
        elif d[i]==1005:
            if d[d[i+1]]!=0:i=d[i+2]
            else:i+=3
        elif d[i]==1105:
            if d[i+1]!=0:i=d[i+2]
            else:i+=3
        elif d[i]==6:
            if d[d[i+1]]==0:i=d[d[i+2]]
            else:i+=3
        elif d[i]==106:
            if d[i+1]==0:i=d[d[i+2]]
            else:i+=3
        elif d[i]==1006:
            if d[d[i+1]]==0:i=d[i+2]
            else:i+=3
        elif d[i]==1106:
            if d[i+1]==0:i=d[i+2]
            else:i+=3
        elif d[i]==7:
            if d[d[i+1]]<d[d[i+2]]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==107:
            if d[i+1]<d[d[i+2]]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==1007:
            if d[d[i+1]]<d[i+2]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==1107:
            if d[i+1]<d[i+2]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==8:
            if d[d[i+1]]==d[d[i+2]]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==108:
            if d[i+1]==d[d[i+2]]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==1008:
            if d[d[i+1]]==d[i+2]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==1108:
            if d[i+1]==d[i+2]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
            
        elif d[i]==99:break
    return r


def ic2(in_,i,d):
    r="exitcode"
    while True:
        if d[i]%10 in (1,2):
            a,b,c=d[i],d[i+1],d[i+2]
            if (a//100)%10==0:b=d[b]
            if a//1000 == 0:c=d[c]
            if a%10==1:rr= b+c
            else:rr= b*c
            d[d[i+3]]=rr
            i+=4
        elif d[i]==3:
            d[d[i+1]]=in_
            i+=2
        elif d[i]==4:
            r=(d[d[i+1]])
            i+=2
            return r,i,d
        elif d[i]==104:
            r=(d[i+1])
            i+=2
            return r,i
        elif d[i]==5:
            if d[d[i+1]]!=0:i=d[d[i+2]]
            else:i+=3
        elif d[i]==105:
            if d[i+1]!=0:i=d[d[i+2]]
            else:i+=3
        elif d[i]==1005:
            if d[d[i+1]]!=0:i=d[i+2]
            else:i+=3
        elif d[i]==1105:
            if d[i+1]!=0:i=d[i+2]
            else:i+=3
        elif d[i]==6:
            if d[d[i+1]]==0:i=d[d[i+2]]
            else:i+=3
        elif d[i]==106:
            if d[i+1]==0:i=d[d[i+2]]
            else:i+=3
        elif d[i]==1006:
            if d[d[i+1]]==0:i=d[i+2]
            else:i+=3
        elif d[i]==1106:
            if d[i+1]==0:i=d[i+2]
            else:i+=3
        elif d[i]==7:
            if d[d[i+1]]<d[d[i+2]]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==107:
            if d[i+1]<d[d[i+2]]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==1007:
            if d[d[i+1]]<d[i+2]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==1107:
            if d[i+1]<d[i+2]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==8:
            if d[d[i+1]]==d[d[i+2]]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==108:
            if d[i+1]==d[d[i+2]]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==1008:
            if d[d[i+1]]==d[i+2]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
        elif d[i]==1108:
            if d[i+1]==d[i+2]:d[d[i+3]]=1
            else:d[d[i+3]]=0
            i+=4
            
        elif d[i]==99:break
    return "exitcode"

m=0
for i in pe((0,1,2,3,4),5):
    a=0
    for j in i:
        a=ic(j,a,[dd for dd in d2])
#        print(i,j,a)
    m=max(m,a)
print(m)
####r,i
m=0
for i in co((9,8,7,6,5),5):
    a=0
    ii=0
    ri=[0,0,0,0,0]
    rout=[[k] for k in i]
    rout=rout[1:]+[rout[0]]
    rds=[[dd for dd in d2] for iii in range(5)]
    rout[4]+=[0]

    while True:
        print(ii,rout)
#        print(i[ii],rout[(ii-1)%5][0],rds[ii])
        while len(rout[(ii-1)%5])==0:
            ii+=1
            ii%=5
            if ii==5:break
        if ii==5:break
        a=ic2(rout[(ii-1)%5][0],ri[ii],rds[ii])
        del rout[(ii-1)%5][0]
        if a=="exitcode":
            if sum(len(h) for h in rout)==0:break
        else:
            ri[ii]=a[1]
            rout[ii]+=[a[0]]
            rds[ii]=a[2]
        ii=(ii+1)%5
        m=max(m,max(max(b+[0]) for b in rout))
print(m)
