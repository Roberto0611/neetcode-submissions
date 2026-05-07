class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest = ""
        count = {}
        OGCount = {}
        l,r = 0,0.
        newr = True

        # is subtring function
        def is_substring(OGCount, count):
            # len filter
            if len(OGCount) > len(count):
                return False
            
            # check one by one
            for c in OGCount:
                if OGCount[c] > count[c]:
                    return False
            return True

        # fist validation
        if len(s) < len(t):
            return shortest
        
        # count t
        for c in t:
            OGCount[c] = OGCount.get(c,0) + 1

        # find starting point
        for i,c in enumerate(s):    
            n = OGCount.get(c,0)
            if n > 0:
                l = i
                r = i
                break

        l = int(l)
        r = int(r)
        print(r)
        # main loop
        while l <= r and r <= len(s) - 1:
            # add the letter if is in OGCount and if r is new
            if newr:
                c = s[r]
                #print(c)
                n = OGCount.get(c,0)
                if n > 0:
                    count[c] = count.get(c,0) + 1
            
            # Compare the dicts
            if is_substring(OGCount,count):
                #print('SUBSTRING')
                if len(s[l:r+1]) < len(shortest) or shortest == "":
                    # new shortest
                    shortest = s[l:r+1]
                # slice the old l value
                c = s[l]
                n = OGCount.get(c,0)
                if n > 0:
                    if count[c] == 1:
                        del count[c]
                    else:
                        count[c] -= 1
                l+=1
                newr = False
                #print(count)
                continue
            
            r += 1
            newr = True;

            #print(count)
        return shortest

