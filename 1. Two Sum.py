from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        #brute force
        for i in range (len(nums) - 1):
            for j in range (i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []



class Test:
    List = [2,7,11,15]
    num = 9

    solution = Solution()
    ris = solution.twoSum(List,num)
    print(ris)