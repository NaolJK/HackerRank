# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
N = int(input())
ans = True


for i in range (N):
    other_set = set(map(int,input().split()))
    isSub = other_set.issubset(A)
    if isSub and len(A) > len(other_set):
        continue
    else:
        ans = False
        break
    
print(ans)
