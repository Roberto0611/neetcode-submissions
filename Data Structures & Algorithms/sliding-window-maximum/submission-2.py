class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = r = 0
        q = collections.deque()

        while r <= len(nums) - 1:
            n = nums[r]

            # delete lower values
            while len(q) != 0 and q[-1] < n:
                q.pop()
            
            # append
            q.append(n)

            if r + 1 >= k:
                output.append(q[0])
                l+=1
                if q[0] == nums[l-1]:
                    q.popleft()

            r+=1

        return output