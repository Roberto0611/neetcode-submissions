class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        TL,Length,maxL,l,r = 0,0,0,0,0
        count = {}

        while l <= r and r <= len(s) - 1:
            count[s[r]] = count.get(s[r],0) + 1
            Length += 1
            TL = abs(max(count.values()) - Length)
            if TL <= k:
                maxL = max(maxL,Length)
                r += 1
                continue
            
            # en caso de que ya no hay comodines
            while not (TL <= k):
                count[s[l]] -= 1
                l += 1
                Length -= 1
                TL = abs(max(count.values()) - Length)
            r+=1 

        return maxL
