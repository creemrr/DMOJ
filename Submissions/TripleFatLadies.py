import sys
n = sys.stdin.read().split()
del n[0]
n = [int(i) for i in n]
for i in n:
    while ((i**3)-888)%1000!=0:
        i+=1
    print(i)