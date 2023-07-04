class Solution:
    def compress(self, chars: list[str]) -> int:
      charsLength = len(chars)
      count = 1

      position = 0

      for index in range(1, charsLength + 1):
        if index < charsLength and chars[index] == chars[index-1]:
          count += 1
          continue

        chars[position] = chars[index - 1]
        position += 1

        if count > 1:
          for digit in str(count):
            chars[position] = digit
            position += 1

        count = 1

      return position
         
      
           
         
    
s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]), 6)
print(s.compress(["a"]), 1)
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]), 4)