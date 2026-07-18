from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set = {}
        result =[]
        for i in range(len(nums)):
            ele = target - nums[i]
            if ele in set:
                result = [set[ele],i]
                break
            else:    
                set[nums[i]] = i
        return result



            
