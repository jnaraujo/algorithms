class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      if len(s) == 0:
        return True
      elif len(t) == 0:
        return False
      
      pos = 0

      for letter in t:
        if letter == s[pos]:
          pos += 1

        if pos > len(s) - 1:
           return True
      return False
    
s = Solution()
print(s.isSubsequence("abc", "ahbgdc"), True)
print(s.isSubsequence("axc", "ahbgdc"), False)
print(s.isSubsequence("ace", "abcde"), True)
print(s.isSubsequence("aec", "abcde"), False)