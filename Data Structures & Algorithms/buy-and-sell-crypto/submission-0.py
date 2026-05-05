class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        j = 1
        sum = 0

        # edge case
        if len(prices) == 0 :
            return 0;
        

        # start loop
        while(j < len(prices)):
            sum = prices[j] - prices[i];
            profit = max(sum,profit)

            if prices[i] > prices[j]:
                i = j
                j += 1
            else:
                j += 1
        return profit


