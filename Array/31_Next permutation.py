'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

# time complexity O(n)

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x = len(nums) - 2
        while x >= 0:
            if nums[x] < nums[x + 1]: break # find the first element smaller than next
            x -= 1
        if x < 0:
            nums.sort() # if it's reversed, sort
            return
        
        y = len(nums) - 1
        while x < y:
            if nums[x] < nums[y]:   # find the first element smaller than x from backward
                break
            y -= 1
        nums[x], nums[y] = nums[y], nums[x] # exchange
        nums[x + 1:] = nums[x + 1:][::-1]   # sort the element after x