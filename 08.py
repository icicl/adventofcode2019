#day 8
with open("08.txt") as f:t = f.read()[:-1]
from PIL import Image as im
m,mv,q = 1000000,0,[[0 for i in range(150)] for j in range(6)]
for i in range(0,len(t),150):
    if t[i:i+150].count('0')<m:mv,m=t[i:i+150].count('1')*t[i:i+150].count('2'),t[i:i+150].count('0')
print(mv)
for i in range(len(t)):
    x,y=i%25,(i%150)//25
    if q[y][x]==0:
        if t[i]=='0':q[y][x]=1
        if t[i]=='1':q[y][x]=2
ii = im.new("RGB",(250,60))
il = ii.load()
for x in range(25):
    for y in range(6):
        for p in range(100):il[10*x+p//10,10*y+p%10]=((255,255,255),(0,0,0))[q[y][x]-1]
ii.show()
