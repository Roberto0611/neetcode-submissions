class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxValue,r = 0,k-1
        output = []
        count = {}

        if nums == []:
            return output

        # get max of first window 
        maxValue = max(nums[:r+1])
        output.append(maxValue)
        
        # count the window
        for number in nums[:r+1]:
            count[number] = count.get(number,0) + 1
        
        # debug
        window = nums[r-(k-1):r+1]
        #print(f'window = {window}')

        # start the main loop
        while(r < len(nums) - 1):
            # move the window
            r+=1

            #print(count)
            window = nums[r-(k-1):r+1]
            #print(f'window = {window}')

            # pop old value
           # print(f'pop: {nums[r-k]}')
            count[nums[r-k]] -= 1;

            if count[nums[r-k]] == 0:
                #print(f'delete {nums[r-k]}')
                del count[nums[r-k]]

            # check the new element
            if window[-1] > maxValue:
                maxValue = window[-1]
            
            count[window[-1]] = count.get(window[-1],0) + 1
            #print(f'just add {window[-1]}')

            # check if the max still exists
            if count.get(maxValue,0) == 0:
                # check for new max...
                maxValue = max(window)

            output.append(maxValue)

        return output