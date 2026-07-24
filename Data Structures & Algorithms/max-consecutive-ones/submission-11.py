class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if(sum(nums) == 0):
            return 0
        else:
            count = 1

        max = 0
        if(len(nums) == 1) and (nums[0] == 1):
            return 1
        for i in range(len(nums)-1):
            if nums[i] == 1 and nums[i+1] == 1:
                count += 1
            else:
                count = 1
            if count >= max :
                max = count
        return max 
        