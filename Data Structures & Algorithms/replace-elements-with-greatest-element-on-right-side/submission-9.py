class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        a = [-1]*l
        if l == 1 :
            a[0] == -1
            return a
        highest = arr[l -1]
        sHighest = arr[l-1]
        prevHighest = arr[l-1]
        
        for i in range(l-2,0,-1):
            if arr[i] > highest:
                sHighest = highest
                highest = arr[i]
                a[i] = sHighest
                continue
            if arr[i] <= arr[i+1] or arr[i] <= highest:
                if arr[i+1] <= highest:
                    a[i] = highest
                else:
                    highest = arr[i+1]
                    a[i] = highest
        a[0] = highest

        return a