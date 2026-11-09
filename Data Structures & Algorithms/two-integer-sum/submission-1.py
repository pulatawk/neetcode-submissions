class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #check if i + j = target 
        #try i with everything (j)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]