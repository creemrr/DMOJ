import sys
n = sys.stdin.read().split('\n')
ct = 0
cs = 0
n = ''.join(n)
for i in n:
    if i=='t' or i=='T':
        ct+=1
    if i=='s' or i=='S':
        cs+=1
if cs>=ct:
    print("French")
else:
    print("English")