# https://leetcode.com/problems/search-insert-position/

import math

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        #     if nums[i] > target:
        #         return i
        #     if i == len(nums) - 1:
        #         return i + 1
        start = 0
        end = len(nums)
        
        while start <= end:
            middle_float = start + end
            middle = (start + end) / 2
            # Target found
            print(middle)
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
    #             search left half
                if start >= end:
                    return middle
                else:
                    # return searchInsert(nums, target, start, middle-1)
                    end = middle - 1
            if nums[middle] < target:
    #             search right half
                if start >= end:
                    return middle + 1
                else:
                    # return searchInsert(nums, target, middle+1, end)
                    start = middle + 1
        if nums[middle] > target:
            if start > end:
                return middle
            else:
                end = middle - 1
        if nums[middle] < target:
#             search right half
            if start > end:
                return middle + 1
            else:
                start = middle + 1
    
        # if len(nums) == 1:
        #     if nums[index] < target:
        #         return index + 1
        #     if nums[index] > target:
        #         # ???
        # if nums[index] == target:
        #     return index
        # if nums[index] > target:
        #     original_index = index
        #     left_half = nums[0 : index]
        #     index = len(nums)
        # if nums[index] < target:
        #     original_index = index
        #     right_half = nums[index : -1]
            
'''
[1,3,5,6]
 0 1 2 3

nums = [1,3,5,6], target = 2
          ^
Loop through the list, the length of the list
keep checking if the current value in the list is the target
If it is the target, return the index
if the current value is greater than the target, return the index
if we reach end of loop, and the current value is still less than the target, return index + 1


Binary Search approach
Get the middle index of the list,
if that current value is equal to target
    return index
if that current value is greater than the target,
    search left half of list,
if that current value is less than the target,
    search right half of list,
    
need to keep track of original index if constantly splitting list in half. 
    
'''
        
