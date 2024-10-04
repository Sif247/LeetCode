from typing import List

# Bad implementations, the complexity is O(n^2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            for j in range(i + 1,len(prices)):
                diff = prices[j] - prices[i]
                if(diff > profit):
                    profit = diff
        return profit


class Test:
    prices = [7,1,5,3,6,4]
    solution = Solution()
    ris = solution.maxProfit(prices)
    print(prices)
    print(ris)
