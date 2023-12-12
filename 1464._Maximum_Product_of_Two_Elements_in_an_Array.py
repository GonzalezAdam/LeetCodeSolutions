class Solution(object):
    def maxProduct(self, nums):
        self.nums = sorted(nums, reverse = True)
        two_numbers = self.nums[:2]
        quotients = []
        for number in two_numbers:
            number = number - 1
            quotients.append(number)
        return quotients[0]*quotients[1]
