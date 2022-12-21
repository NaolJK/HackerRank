from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
ele = int(input())
total_words = {}

for i in range(0, ele):
    words = input()

    if words not in total_words:
        total_words[words] = 1
    else:
        total_words[words] += 1

total_len = len(total_words)
string = list(map(str, list((total_words.values()))))


print(total_len)
print(" ".join(string))
