class Solution:
    def calPoints(self, ops: List[str]) -> int:
        a = []
        sum = 0
        last = 0
        for i in ops:
            if i == 'C':
                a.pop()
            elif i == 'D':
                last  = a.pop()
                a.append(int(last))
                a.append(2*int(last))
            elif i == '+':
                first = a.pop()
                second = a.pop()
                a.append(int(second))
                a.append(int(first))
                a.append(int(first) + int(second))
            else :
                a.append(int(i))

        for i in a:
            sum += i
        return(sum)
            
        