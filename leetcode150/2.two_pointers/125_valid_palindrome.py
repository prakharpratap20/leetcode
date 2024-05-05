"""
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s) -1

        while l < r:
            while l < r and not self.alphaNum(s[r]):
                l += 1
            while l < r and not self.alphaNum(s[l]):
                r -= 1
            if s[l].lower()!= s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9"))
    

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))