class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        r = k - 1
        OGCount = {}
        count = {}
        
        # count s1
        for c in s1:
            OGCount[c] = OGCount.get(c,0) + 1

        # count k elements in s2
        for c in s2[:k]:
            count[c] = count.get(c,0) + 1

        if OGCount == count:
            return True;
    
        # start window loop
        while(r < len(s2) - 1):
            print(f'og {OGCount}')
            print(f'normal {count}')
            r+=1
            count[s2[r]] = count.get(s2[r],0) + 1
            count[s2[r-k]] -= 1
            if count[s2[r-k]] == 0:
                del count[s2[r-k]]
            if OGCount == count:
                return True;

        return False