from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        countZero = 0
        countOther = 0
        i = 0
        while i < (len(nums) - 1):
            if nums[i] == 0:
                nums.remove(0)
                i -= 1
                countZero += 1
            else:
                countOther += 1
            i += 1

        for j in range (countZero):
            countOther += 1
            nums.insert(countOther, 0)



class Test:
    s1 = [0, 1, 0, 3, 12]
    s2 = [0]

    solution = Solution()
    solution.moveZeroes(s1)
    solution.moveZeroes(s2)

    print(s1)
    print(s2)