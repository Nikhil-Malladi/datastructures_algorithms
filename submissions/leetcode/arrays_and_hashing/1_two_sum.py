class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashset=dict()
        for e,i in enumerate(nums):
            diff=target - i
            if diff in hashset:
                return [hashset[diff],e]
            hashset[i]=e
