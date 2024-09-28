class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Brute Force

        if not nums:
            return 0

        self = len(nums)

        i = 0
        for j in range (1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1




class Test():
    nums = [0,0,1,1,1,2,2,3,3,4]


    ris = Solution.removeDuplicates(0, nums)

    print(ris)
    print(nums)