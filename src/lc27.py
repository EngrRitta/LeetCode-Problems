class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        writePointer = 0
        count = 0
        for searchPointer in range(len(nums)):
            if nums[searchPointer] != val:
                count = count + 1
                nums[writePointer] = nums[searchPointer]
                writePointer = writePointer + 1
        return count