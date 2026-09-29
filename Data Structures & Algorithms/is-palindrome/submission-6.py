class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char.lower() for char in s if char.isalnum())
        start ,last  = 0 , len(string)
        for i in range(len(string)):

            if string[start] == string[last-1]:
                start += 1
                last -= 1
            else :
                return False
        return True
        