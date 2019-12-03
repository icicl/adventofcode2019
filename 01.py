with open("01.txt") as f:d = [int(i) for i in f.read()[:-1].split('\n')]
print(sum(i//3-2 for i in d))
def f(n):return 0 if n<9 else n//3-2+f(n//3-2)
print(sum(f(i) for i in d))
