with open("06.txt") as f:q = {i.split(')')[1]:i.split(')')[0] for i in f.read()[:-1].split('\n')}
q2,m=dict(q),{'COM':0}
while sum(len(q[i]) for i in q)>0:
    for i in q:
        if q[i] in m:m[i],q[i]=m[q[i]]+1,''
print(sum(m[i] for i in m))
def has(o,i,d=0):
    if o==i:return d
    if not o in q2:return False
    return has(q2[o],i,d+1)
print(min(has('YOU',i)+has('SAN',i)-2 for i in q2 if has('YOU',i) and has('SAN',i)))
