class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = -1
        r = 0
        length = 0
        maxLength = 0
        sCount = dict()

        while(r > l and r <= len(s) - 1):
            # si ya tenemos el valor...
            if sCount.get(s[r]) == 1:
                print(f'valor repetido {s[r]}')
                l+=1
                sCount[s[l]] -= 1
                length -= 1
                continue

            # si no tenemos el valor
            sCount[s[r]] = 1
            r+=1
            length += 1

            # actualizar maxLength
            maxLength = max(length,maxLength)
            print(f'length {maxLength}')
            print(sCount)

        return maxLength