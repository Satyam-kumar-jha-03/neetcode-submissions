class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = len(nums)
        set = defaultdict(int)

        for i in nums:
            set[i] += 1
        result = sorted(set, key = set.get , reverse = True)[:1]
        result.append(int(-sum(nums)+result[0] + s*(s+1)/2))
        return(result)
        

             
        

        