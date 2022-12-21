# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
number_of_groups = input()
number_of_rooms = input()
number_of_rooms = number_of_rooms.split()
number_of_rooms = list(map(int,number_of_rooms))

freq = (dict(Counter(number_of_rooms)))
capitain = 0 
for key,value in freq.items():
    if value == 1:
        capitain = key
        
print(capitain)
