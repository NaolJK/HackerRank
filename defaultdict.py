from collections import defaultdict
size_a, size_b = map(int, input().split())


a = defaultdict(list)

for i in range (size_a):
    elem = input()
    a[elem].append(str(i+1)) 

for i in range (size_b):
    el = input()
    if el in a:
        res = " ".join(a[el])
        print(res)
    else:
        print(-1)
