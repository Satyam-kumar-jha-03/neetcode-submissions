class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = 0

        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
                count += 1
    
        return(count)

        