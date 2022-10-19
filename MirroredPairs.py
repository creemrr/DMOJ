import sys
n = sys.stdin.read().split('\n')
print("Ready")
x = ['pq', 'qp', 'db', 'bd']
for i in n:
    if i=='  ':
        break
    elif i in x:
        print("Mirrored pair")
    else:
        print("Ordinary pair")