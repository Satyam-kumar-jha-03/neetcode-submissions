class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sum1 , prod1 , xor1 = 0,1,1
        sum2 , prod2 , xor2 = 0,1,1
        for i in s:
            sum1 += ord(i)
            prod1 *= ord(i)
            xor1 ^= ord(i)

        for j in t:
            sum2 += ord(j)
            prod2 *= ord(j)
            xor2 ^= ord(j)

        if sum1 == sum2 and prod1 == prod2 :
            if xor1 == xor2:
                return(True)
            else:
                return(False)
        else:
            return(False)