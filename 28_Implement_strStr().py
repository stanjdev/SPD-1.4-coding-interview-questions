# https://leetcode.com/problems/implement-strstr/

""" 
Success! 
Runtime: 27 ms, faster than 78.92% of Python online submissions for Implement strStr().
Memory Usage: 15.1 MB, less than 8.14% of Python online submissions for Implement strStr().
 """

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        last_index_needle = len(needle) - 1
        if not needle or needle == haystack:
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if needle[0] == haystack[i] and needle[last_index_needle] == haystack[i + last_index_needle]:
                # enter a sub loop
                for j in range(len(needle)):
                    if needle[j] != haystack[i + j]:
                        break
                    if j == len(needle) - 1:
                        return i
        return -1
                    
'''
mississippi
 issip
'''
            
        
'''
In a string of haystack, return the first index of needle string if it is found in the haystack.
What if the needle is an empty string? 

Check to see if a string is found in another string. Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Input: haystack = "hello", needle = "ll"
Output: 2

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Input: haystack = "", needle = ""
Output: 0

Input: haystack = "a", needle = "a"
Output: -1 (not found???)

Input: haystack = "abc", needle = "c"
Output: 2

Input: haystack = "mississippi", needle = "issip"
Output: 4


Pseudocode:
if needle is empty string, return 0
Remember the length of the needle (2 for "ll")
loop through haystack
    if the first character of the needle[0] == current haystack character,
    enter a loop to check if the rest of the characters all match. 
    if you reach the end of the sub-loop, 
        return the index of the outer loop as you found it
    else:
        continue the outer loop
if you reach here, it was not found. return -1
    
'''
