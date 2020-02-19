class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(nums, target, left):
            l = 0
            r = len(nums)
            while l < r:
                pivot = l + (r-l)//2
                if nums[pivot] > target or (left and target == nums[pivot]):
                    r = pivot
                else:
                    l = pivot + 1
            
            return l
        
        left_idx = binarySearch(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return -1,-1
        return [left_idx, binarySearch(nums, target, False)-1]
            