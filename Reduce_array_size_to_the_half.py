import math
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequency = dict(Counter(arr))
        frequency_list = list(frequency.values())
        
        frequency_list.sort(reverse=True)
        min_set_size = 0
        result = 0
        for i in frequency_list:
            result+= i
            min_set_size +=1
            # print(math.ceil(len(arr)/2))
            if result >= math.ceil(len(arr)/2):
                break
        return min_set_size
            
            
            
            