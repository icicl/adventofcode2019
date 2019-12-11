with open("05.txt") as f:
    q=f.read()[:-1].split(',')

d=[int(i) for i in q]
i=0
in_=1
def  _12(a,b,c):
    if (a//100)%10==0:b=d[b]
    if a//1000 == 0:c=d[c]
    if a%10==1:return b+c
    return b*c

while True:
    if d[i]%10 in (1,2):
        d[d[i+3]]=_12(d[i],d[i+1],d[i+2])
        i+=4
    elif d[i]==3:
        d[d[i+1]]=in_
        i+=2
    elif d[i]==4:
        if d[d[i+1]]!=0:print(d[d[i+1]])
        i+=2
    elif d[i]==104:
        if d[i+1]!=0:print(d[i+1])
        i+=2
    elif d[i]==99:break
d=[int(i) for i in q]
i=0
ins=[5]
while True:
    if d[i]%10 in (1,2):
        d[d[i+3]]=_12(d[i],d[i+1],d[i+2])
        i+=4
    elif d[i]==3:
        d[d[i+1]]=ins[0]
        i+=2
    elif d[i]==4:
        print(d[d[i+1]])
        i+=2
    elif d[i]==104:
        print(d[i+1])
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
    else:print(d[i:i+4])
