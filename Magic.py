import sys
n = sys.stdin.read().split()
n = [int(i) for i in n]
fr = sum(n[0:4])
sr = sum(n[4:8])
tr = sum(n[8:12])
foro = sum(n[12:16])
fc = sum(n[0:16:4])
sc = sum(n[1:16:4])
tc = sum(n[2:16:4])
foc = sum(n[3:16:4])
if sr==fr and tr==fr and foro==fr and fc==fr and sc==fr and tc==fr and foc==fr:
    print('magic')
else:
    print('not magic')