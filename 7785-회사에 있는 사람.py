import sys

log = {}

result = []
for i in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().rstrip().split()
    if a[1] == 'enter':
        log[a[0]] = 'enter'
    else:
        del log[a[0]]

for i in sorted(log, reverse=True):
    print(i)    

