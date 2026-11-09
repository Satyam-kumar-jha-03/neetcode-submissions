class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j  = 0 , len(nums)-1
        result = []*2
        for k in range(j):
            sum = nums[i] + nums[j]
            if sum == target:
                result.append(i+1)
                result.append(j+1)
                break
            if sum > target:
                j -= 1
            else:
                i += 1
            
        return result

            
        