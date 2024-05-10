class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = len(nums) - 1
        ans = range(len(nums) * 2)
        while i > -(len(nums) + 1):
            ans[i] = nums[i]
            i = i - 1
        return ans
