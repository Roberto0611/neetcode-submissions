class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        TL,Length,maxL,l,r = 0,0,0,0,0
        count = {}

        while l <= r and r <= len(s) - 1:
            #print(f'revisando {s[r]}')
            count[s[r]] = count.get(s[r],0) + 1
            Length += 1
            #print(count)
            #print(f'length {Length}')
            TL = abs(max(count.values()) - Length)
           # print(f'TL: {TL}')
            if TL <= k:
                maxL = max(maxL,Length)
                #print(f'MAXL: {maxL}')
                r += 1
                continue
            
            # en caso de que ya no hay comodines
            while not (TL <= k):
                #print('Recalculando l')
                count[s[l]] -= 1
                l += 1
                Length -= 1
                TL = abs(max(count.values()) - Length)
                #print(f'paso, Length {Length}, TL {TL}')
            r+=1 
            #print('saliendo')

        return maxL
