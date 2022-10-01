class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range (0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] > nums[j]):
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        result=[]
        for i in range (0,len(nums)):
            if nums[i] == target:
                result.append(i)
        return result
        