class Solution:
    def sortArray(self, a: List[int]) -> List[int]:
        def mergesort(a,l,r):
            if l < r:
                m  = l + (r-l)//2
                mergesort(a,l,m)
                mergesort(a,m+1,r)
                merge(a,l,m,r)

        def merge(a,l,m,r):
            i , j, k = l,m+1,l
            while(i <= m and j <= r):
                if a[i] < a[j]:
                    b[k] = a[i]
                    i += 1
                else:
                    b[k] = a[j]
                    j += 1
                k += 1
            while i <= m:
                b[k] = a[i]
                i += 1
                k += 1
            while j <= r:
                b[k] = a[j]
                j += 1
                k += 1
            for i in range(l,r+1):
                a[i] = b[i]
        b = [0]*len(a)
        mergesort(a,0,len(a)-1)
        
        return a
        
        