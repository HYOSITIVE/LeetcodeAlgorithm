class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = []
        for letter in s :
            if letter.isalnum():
              original.append(letter.lower())
        while len(original) > 1:
          if original.pop(0) != original.pop():
            return False
        return True