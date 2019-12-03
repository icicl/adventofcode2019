year = '2019'
day = '01'#the day of the problem, from 1 to 25

from itertools import combinations as combs###
from itertools import permutations as perms###sometimes useful, and saves me the time typing it
import hashlib
def md5(x):return hashlib.md5(x.encode()).hexdigest()#doesnt seem likely, but may be used 1 day this year

from os.path import exists, getsize
import requests
if not exists(day+'.txt') or getsize(day+'.txt')==0:
    with open(day+'.txt','w+') as f:
        h = {'Cookie':'session=[your token: 96 digit hex string]'}
        url = 'https://adventofcode.com/'+year+'/day/'+str(int(day))+'/input'
        f.write(requests.get(url,headers=h).text)

import re
with open(day+".txt") as f:
    t = f.read()[:-1]
q = t.split('\n')#input split by line
d = [[int(i) for i in re.findall('-?\d+',j)] for j in q]#all integers from input


