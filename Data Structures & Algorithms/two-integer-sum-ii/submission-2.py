class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set = {}
        result =[]
        for i in range(len(nums)):
            ele = target - nums[i]
            if ele in set:
                result = [set[ele]+1,i+1]
                break
            else:    
                set[nums[i]] = i
        return result
        