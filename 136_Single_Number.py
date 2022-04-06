# https://leetcode.com/problems/single-number/

""" 
Success:
Runtime: 162 ms, faster than 48.56% of Python online submissions for Single Number.
Memory Usage: 15.6 MB, less than 65.70% of Python online submissions for Single Number.
 """

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         Using a dict to find if a number key only appears once.
#         if len(nums) == 1:
#             return nums[0]
#         my_dict = {}
#         for i in range(len(nums)):
#             if nums[i] not in my_dict:
#                 my_dict[nums[i]] = 1
#             else:
#                 my_dict[nums[i]] += 1
#         list_of_entries = my_dict.items()
        
#         for pair in list_of_entries:
#             if pair[1] == 1:
#                 return pair[0]
        
#     Sorting first, then iterating by 2, finding a non-pair number
        nums.sort()
        curr = 0
#         ITERATE BY 2 INSTEAD
        for i in range(0, len(nums) - 1, 2):
            curr = nums[i]
            if curr == nums[i + 1]:
                continue
            else: 
                return curr
        return nums[-1]
        
    
        """
        current_number = 1
        [1, 2, 2]
        
        sort list
        current_number = 2
        [1, 1, 2, 2, 4]
                     ^
        
        
        Input: nums = [4,1,2,1,2]
                         ^
        Output: 4
        
        {
            4: 1,
            1: 2,
            2: 2,
        }
        [[4, 1], [1, 2], [2, 2]]
        
        input: nums = [2, 2, 1]
        
        output: 1
        
        Input: nums = [1]
        Output: 1
        
        
        {
            2: 2
            1: 1
        }
        
        if len(num) == 1
            return num[0]
        
        create dictionary {}
        loop through the nums:
            if num isn't found in dict,
                add that key to dict with count of 1
            else:
                increment that count to make it 2
            
        method to turn dict into array of [[key, value], ] , iterate through this array, find that value of 1, and return that key
        
        """
        
        
        
        
        