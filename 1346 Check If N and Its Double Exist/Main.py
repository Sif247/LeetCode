from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] == 2 * arr[j] or arr[i] == arr[j] / 2:
                    return True

        return False

class Test:
    s1 = [10,2,5,3]
    s2 = [3,1,7,11]

    solution = Solution()
    ris = solution.checkIfExist(s1)
    ris2 = solution.checkIfExist((s2))

    print(ris)
    print(ris2)


