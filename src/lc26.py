class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        count = 1
        writePointer = 0
        for readPointer in range(len(nums)):
            if nums[writePointer] != nums[readPointer]:
                count = count + 1
                nums[writePointer + 1] = nums[readPointer]
                writePointer = writePointer + 1
        return count