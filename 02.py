with open("02.txt") as f:
    q=f.read()[:-1].split(',')

d=[int(i) for i in q]
d[1],d[2],i=12,2,0
while True:
    if d[i]==1:d[d[i+3]]=d[d[i+1]]+d[d[i+2]]
    elif d[i]==2:d[d[i+3]]=d[d[i+1]]*d[d[i+2]]
    elif d[i]==99:break
    i+=4
print(d[0])
       
for n in range(10000):
    d=[int(i) for i in q]
    d[1],d[2],i=n//100,n%100,0
    while True:
        if d[i]==1:d[d[i+3]]=d[d[i+1]]+d[d[i+2]]
        elif d[i]==2:d[d[i+3]]=d[d[i+1]]*d[d[i+2]]
        elif d[i]==99:break
        i+=4
    if d[0]==19690720:print(n)
