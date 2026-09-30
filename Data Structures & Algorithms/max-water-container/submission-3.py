class Solution:
    def maxArea(self, h: List[int]) -> int:
        start , last  = 0 , len(h)-1
        maxw = (min(h[start],h[last]))*(last-start)
        water = 0

        for i in range(last):
            water = (min(h[start],h[last]))*(last-start)
            if water > maxw :
                maxw = water
            if h[start] > h[last]:
                last -= 1
            else:
                start += 1
        return maxw
            


        