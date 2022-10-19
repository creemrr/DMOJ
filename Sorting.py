import sys
n = sys.stdin.read().split()
del n[0]
n = [int(i) for i in n]
n.sort()
for i in n:
    print(i)