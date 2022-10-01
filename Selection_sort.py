#User function Template for python3

class Solution: 
    def select(self, arr, i):
        array_length = len(arr)
        minimum = i
        for j in range(i+1,array_length):
            if arr[j] < arr[minimum]:
                minimum = j
        
        return minimum
        
        # code here 
    
    def selectionSort(self, arr,n):
        for i in range (0,n):
            min_index = self.select(arr,i)
            temp = arr[min_index]
            arr[min_index] = arr[i]
            arr[i] = temps