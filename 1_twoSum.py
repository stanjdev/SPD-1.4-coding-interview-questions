# https://leetcode.com/problems/two-sum/

""" 
Success!
Runtime: 55 ms, faster than 80.52% of Python online submissions for Two Sum.
Memory Usage: 14.2 MB, less than 86.95% of Python online submissions for Two Sum.
Runtime: 43 ms, faster than 94.85% of Python online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 45.87% of Python online submissions for Two Sum.
Runtime: 40 ms, faster than 97.93% of Python online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 23.18% of Python online submissions for Two Sum.

GIVEN INPUT: list of numbers, and a target number
OUTPUT: a list pair of indexes (ex. [i, j])

 """

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Hash map method:
        seen = {}
        for i in range(len(nums)):
            if not nums[i] in seen:
                seen[nums[i]] = i
            # always one step ahead:
            if (target - nums[i + 1]) in seen:
                return [seen[target - nums[i + 1]], i + 1]
            
            
        """
        seen = {
            2: 0,
            7: 1,
            
        }
        """
        
        # # Brute force double-loop:
        # # Loop through the list:
        # for i in range(len(nums)):
        #     # for every element, loop from this element's index + 1 to the end of the list
        #     for j in range(i + 1, len(nums)):
        #         # if the sum of the pair equals the target, return both indexes
        #         sum = nums[i] + nums[j]
        #         if sum == target:
        #             return [i, j]
        