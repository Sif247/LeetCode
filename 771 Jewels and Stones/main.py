
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0
        for stone in stones:
            if stone in s:
                count += 1
        return count

class Test:
    solution = Solution()
    jewels = "aA"
    stones = "aAAbbbb"
    ris = solution.numJewelsInStones(jewels, stones)
    print(ris)

    jewels1 = "z"
    stones1 = "ZZ"
    ris2 = solution.numJewelsInStones(jewels1, stones1)
    print(ris2)
