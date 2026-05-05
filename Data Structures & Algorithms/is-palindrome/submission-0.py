class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = 0
        b = len(s) - 1
        while a < b:
            if not s[a].isalnum():
                a+=1 
                continue
            if not s[b].isalnum():
                b-=1
                continue
            if s[a] != s[b]:
                return False
            a+=1
            b-=1
        return True
            
        