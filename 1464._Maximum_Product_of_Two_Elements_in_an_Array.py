class Solution(object):
    def maxProduct(self, nums):
        self.nums = sorted(nums, reverse = True)
        two_numbers = self.nums[:2]
        return (two_numbers[0]-1)*(two_numbers[1]-1)
