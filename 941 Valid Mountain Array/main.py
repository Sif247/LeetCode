from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        numlen = len(arr)
        if numlen < 3 or arr[0] > arr[1]:
            return False
        count = 0
        for i in range(numlen - 1):
            if arr[i] == arr[i + 1]:
                return False
            elif arr[i] < arr[i + 1]:
                count += 1
            else:
                break

        if numlen == count + 1:
            return False

        for i in range(count, numlen - 1):
            if arr[i] == arr[i + 1] or arr[i] < arr[i + 1]:
                return False

        return True


class Test:
    solution = Solution()


    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ris = solution.validMountainArray(arr)
    print(ris)

    arr2 = [3,5,5]
    ris2 = solution.validMountainArray(arr2)
    print(ris2)

    arr3 = [0,3,2,1]
    ris3 = solution.validMountainArray(arr3)
    print(ris3)

