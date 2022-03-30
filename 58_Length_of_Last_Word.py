# https://leetcode.com/problems/length-of-last-word/
""" 
Success:
Runtime: 18 ms, faster than 77.45% of Python online submissions for Length of Last Word.
Memory Usage: 13.8 MB, less than 28.78% of Python online submissions for Length of Last Word.
 """


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        '''
        Return the length of the last word in a given string with spaces

        Given: s = "a "
        Output: 1
        
        Given: s = "   fly me   to   the moon  "
        Output: 4
        
        have a variable holding onto last_word
        have word_start, and word_end pointers
        reverse loop through string from end, 
            if not a space, mark the word_end pointer there,
            and if you hit another space, mark word_start pointer there,
            store word in last_word, until you hit a space, following another non-space character to save a new last_word
            Once you have the last word, return length of it.
            
            or alternatively, you can reverse concatenate the word with shift() or something or string reversal
        '''
        last_word = ""
        word_end = len(s) - 1
        word_start = 0
        on_char = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " " and on_char == False:
                word_end = i
                on_char = True
            if s[i] != " ":
                on_char = True
            if s[i] == " " and on_char == True:
                word_start = i + 1
                on_char = False
                break
        return word_end - word_start + 1
                
        # # Simple way using methods:
        # # Use strip() to strip away spaces
        # # Grab last element in array, return its length
        # s = s.strip().split(' ')
        # return len(s[len(s) - 1])
                
        """
        last_word = ""
        word_start = 0
        word_end = 0
        on_char = True
        "a "
         ^
        
        last_word = ""
        word_start = 6
        word_end = 10
        on_char = True
        "Hello World"
              ^
        
        last_word = ""
        word_start = 0
        word_end = index of 'n'
        on_char = True
        "   fly me   to   the moon  "
                             ^
        """
        
        