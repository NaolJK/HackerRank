set_len = input().split()
arr_elem = (input().split())
set_a = set(input().split())
set_b = set(input().split())

count = 0 
for i in arr_elem:
    if i in set_a:
        count+=1
    if i in set_b:
        count-=1
print(count)
    
