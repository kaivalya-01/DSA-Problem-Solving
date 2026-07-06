Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

class Solution(object):
    def findGCD(self, nums):
        smallest = min(nums)
        largest = max(nums)

        while largest % smallest != 0:
            smallest, largest = largest % smallest, smallest

        return smallest
