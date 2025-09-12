# My Explanation:
"""
We have two variables or pointers = left and right
left -> points to the beginning of the input string
right -> points to the last index of the input string

we then iterate from left -> right and left <- right until the two pointers meet
    * if the character in the string we encounter is not alphanumeric at either end, move the index until we encounter one

    compare the str[left] and str[right]:
        if they don't match, this cannot be a palindrome - return false

if the flow of the algorithm reaches this point withing hittin one of the conditions above then it is a palindrome

"""


def is_palindrome(s):
  left, right = 0, len(s) - 1

  while left < right:
      while left < right and not s[left].isalnum():
        left += 1

      while left < right and not s[right].isalnum():
        right -= 1

      if s[left].lower() != s[right].lower():
        return False
      
      left += 1
      right -= 1

  return True