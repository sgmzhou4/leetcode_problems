'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

# time complexity O(log(n))

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearchFirst():
            left, right = 0, len(nums) - 1
            l = -1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    l = mid
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return l
        
        def binarySearchLast():
            left, right = 0, len(nums) - 1
            r = -1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    r = mid
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return r
        
        l = binarySearchFirst()
        r = binarySearchLast()
        return [l,r]