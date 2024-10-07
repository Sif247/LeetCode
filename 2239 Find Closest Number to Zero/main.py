import math
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        distance = math.fabs(0 - nums[0])
        ris = 0
        for i in range(1, len(nums)):
            if nums[i] == 0:
                return 0
            elif math.fabs(0 - nums[i]) < distance:
                distance = math.fabs(0 - nums[i])
                ris = i
            elif math.fabs(0 - nums[i]) == distance:
                if nums[i] > nums[ris]:
                    ris = i
        return nums[ris]

class Test:
    solution = Solution()
    nums = [-4, -2, 1, 4, 8]
    ris = solution.findClosestNumber(nums)
    print(ris)

    nums2 = [2, -1, 1]
    ris2 = solution.findClosestNumber(nums2)
    print(ris2)



