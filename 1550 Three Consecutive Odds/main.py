from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            if arr[i] % 2 != 0 :
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False

class Test:
    arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    solution = Solution()
    ris1 = solution.threeConsecutiveOdds(arr)
    print(ris1)

    arr2 = [2, 6, 4, 1]
    ris2 = solution.threeConsecutiveOdds(arr2)
    print(ris2)

    