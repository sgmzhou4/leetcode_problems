class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:    # using binary search
            pivot = left + (right - left)//2    # pivot element
            if nums[pivot] == target:   # return target
                return pivot
            if nums[pivot] >= nums[left]:
                if nums[pivot] > target and target >= nums[left]:   # both target and pivot on the left side && target < pivot.val
                    right = pivot-1
                else:
                    left = pivot+1
            else:
                if nums[pivot] < target and target <= nums[right]:  # both target and pivot on the right side && target > pivot.val
                    left = pivot+1
                else:
                    right = pivot-1
        return -1


test = Solution()
a = test.search([1,4,6,2,8,0,5], 5)
print(a)