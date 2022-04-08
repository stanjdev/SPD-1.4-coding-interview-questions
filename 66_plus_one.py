# https://leetcode.com/problems/plus-one/
""" 
Success
Runtime: 33 ms, faster than 26.14% of Python online submissions for Plus One.
Memory Usage: 13.3 MB, less than 71.06% of Python online submissions for Plus One.
 """

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # # Simple using methods to convert back and forth from ints to strings
        # str1 = "".join(str(e) for e in digits)
        # list1 = list(str(int(str1) + 1))
        # return [int(e) for e in list1]
        
        '''
        Given: [8,9,9,9]
        
        Output: [9,0,0,0]
                 ^
        index: 3
        '''
        
        index = len(digits) - 1
        while digits[index] == 9:
            digits[index] = 0
            if index == 0:
                digits.insert(0, 1)
                return digits
            if digits[index - 1] != 9:
                digits[index - 1] += 1
                return digits
            index -= 1
        digits[index] += 1
        return digits
            

        # grab the last element of the list
        # while it is 9, turn it into a 0
            # and increment the preceding number
            # repeat if that preceding number was also a 9.
            # if preceding number is not a 9, just increment it like normal, then return because no more operations are needed
            # if preceding number is out of range (beginning of array), must insert a 1 to the beginning of the array. return the array. 
        # else, increment the digit it by 1
        # return the list
        
        """
        Add 1 to an array of digits as if it were a whole number
        Given: [9, 9, 9, 9]
        Output: [1, 0, 0, 0, 0]
        
        Given: [9, 9]
        Output: [1, 0, 0]
        """
    
    