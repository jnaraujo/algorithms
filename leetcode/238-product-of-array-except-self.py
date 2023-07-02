class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
      mult = 1
      zeroes = 0
      pos = -1

      for index, num in enumerate(nums):
        if num == 0:
          zeroes += 1
          num = 1
          pos = index
        
        if zeroes > 1:
          return [0] * len(nums)
        
        mult *= num

      if zeroes:
        result = [0] * len(nums)
        result[pos] = mult
        return result

      return [mult // num for num in nums]

s = Solution()
print(s.productExceptSelf([1,2,3,4]) == [24,12,8,6])
print(s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0])
print(s.productExceptSelf([1,2,3,4]))