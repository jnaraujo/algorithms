class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        queue = []

        word = list(s)

        for letter in s:
            if letter in VOWELS:
                queue.append(letter)

        for index, letter in enumerate(s):
            if letter in VOWELS:
                word[index] = queue.pop()

        return "".join(word)
    

s = Solution()
print(s.reverseVowels("hello") == "holle")
print(s.reverseVowels("leetcode") == "leotcede")