class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)
    
s = Solution()
print(s.reverseWords("the sky is blue") == "blue is sky the")
print(s.reverseWords("  hello world  ") == "world hello")
print(s.reverseWords("a good   example") == "example good a")