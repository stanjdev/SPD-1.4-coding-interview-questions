# https://leetcode.com/problems/longest-common-prefix/
""" 
Success!
Sorting first:
Runtime: 32 ms, faster than 47.16% of Python online submissions for Longest Common Prefix.
Memory Usage: 13.6 MB, less than 63.15% of Python online submissions for Longest Common Prefix.

Runtime: 20 ms, faster than 91.13% of Python online submissions for Longest Common Prefix.
Memory Usage: 13.6 MB, less than 63.15% of Python online submissions for Longest Common Prefix.

Runtime: 41 ms, faster than 22.80% of Python online submissions for Longest Common Prefix.
Memory Usage: 13.6 MB, less than 63.15% of Python online submissions for Longest Common Prefix.

Runtime: 28 ms, faster than 62.25% of Python online submissions for Longest Common Prefix.
Memory Usage: 13.6 MB, less than 86.25% of Python online submissions for Longest Common Prefix.


Unsorted:
Runtime: 24 ms, faster than 78.46% of Python online submissions for Longest Common Prefix.
Memory Usage: 13.6 MB, less than 63.15% of Python online submissions for Longest Common Prefix.

Runtime: 33 ms, faster than 43.41% of Python online submissions for Longest Common Prefix.
Memory Usage: 13.6 MB, less than 86.25% of Python online submissions for Longest Common Prefix.

Runtime: 41 ms, faster than 22.80% of Python online submissions for Longest Common Prefix.
Memory Usage: 13.5 MB, less than 86.25% of Python online submissions for Longest Common Prefix.
 """


""" 
Write a function to find the longest common prefix string amongst an array of strings. 
If there is no common prefix, return an empty string "".

Given: strs: list of strings
Output:

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
 
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        ''' Another way is to first sort strs by length in asc order first 
        and then short-check the shortest words to the following ones '''
        ## Sorting first:
#         def by_length(e):
#             return len(e)
#         strs.sort(key=by_length)
        
#         prefix_string = ""
#         first_word = strs[0]
#         # loop the letters of first word:
#         for i in range(len(first_word)):
#             # loop through the list of words starting from second word:
#             for j in range(1, len(strs)):
#                 # check if current letter of first word equals current letter of next words # if any mismatch, return prefix_string
#                 if first_word[i] != strs[j][i]:
#                     return prefix_string
#              # if made it all the way to the end of list of words, concatenate prefix_string with letter
#             prefix_string += first_word[i]
#         return prefix_string
        
        ## Unsorted:
        prefix_string = ""
        first_word = strs[0]
        # loop the letters of first word:
        for i in range(len(first_word)):
            # loop through the list of words starting from second word:
            for j in range(1, len(strs)):
                # check if current letter of first word equals current 
                # letter of next words # if any mismatch, return prefix_string
                if (len(strs[j]) - 1) < i or first_word[i] != strs[j][i]:
                    return prefix_string
             # if made it all the way to the end of list of words, 
             # concatenate prefix_string with letter
            prefix_string += first_word[i]
        return prefix_string

""" 
Input: strs = ["flower","flow","flight"]
Output: "fl"

FIRST ITERATION:

prefix_string = ""
first_word = "flower"
first_word[i] = "f"
strs[j][i] = "f"

prefix_string = ""
first_word = "flower"
first_word[i] = "f"
strs[j][i] = "f"


SECOND ITERATION:

prefix_string = "f"
first_word = "flower"
first_word[i] = "l"
strs[j][i] = "l"

prefix_string = "f"
first_word = "flower"
first_word[i] = "l"
strs[j][i] = "l"


THIRD ITERATION:

prefix_string = "fl"
first_word = "flower"
first_word[i] = "o"
strs[j][i] = "o"

prefix_string = "fl"
first_word = "flower"
first_word[i] = "o"
strs[j][i] = "i"


return prefix_string = "fl"

 """

