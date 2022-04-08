""" 
def isAnagram(list_of_strings):
  sort both words, and compare and if they're the same, return true
  OR
  histogram both words, return if histograms are exactly the same


Given input: list_of_strings = ["listen", "silent"]
Output = true

Given input: ["fried", "fired"]
Output = true

Given input: ["a gentleman", "elegant man"]
Output = true

Given input: ["", ""]
Output = true

Given input: ["of", ""]
Output = false

Given input: ["triangle", "integral"]
Output = true

Given input: ["dolphin", "pokemon"]
Output = false

Given input: ["anagram", "grammar"]
Output = false

Given input: ["anagram", "margana"]
Output = true

Given input: ["elvis", "lives"]
Output = true



LEVEL TWO: strings of different lengths, but check if either word can be spelled by letters in the opposite string

Given input: ["listen", "gistening"]
Output = true
  
  check each letter in first word, delete the found letters in second word
  if leftover letters in left word, false
  
  or histogram approach, compare histograms




LEVEL THREE: 3 strings in a given list, check if all three are interchangeably anagrams

Given input: ["listen", "glistening", "sodapop"]
Output = false

Given input: ["auctioned", "cautioned", "education"]
Output = true



 """











""" 
OTHER IDEAS:
time zones?

ascii code and string letters

spell out a string using only prime numbers

is valid rgb number (130, 254, -8) - too easy
given 1094 - invalid. can it be divied up into valid rgb number? 
-675 - invalid
450 - valid

 """
