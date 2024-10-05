from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for i in range (len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.append(nums[i])
        return False

class Test:
    nums = [1, 2, 3, 1]
    solution = Solution()
    ris = solution.containsDuplicate(nums)
    print(ris)

    nums2 = [1,2,3,4]
    ris2 = solution.containsDuplicate(nums2)
    print(ris2)