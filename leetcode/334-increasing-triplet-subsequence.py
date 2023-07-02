class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
      n1 = n2 = float('inf') 

      for num in nums:
        if num <= n1:
          n1 = num
        elif num <= n2:
          n2 = num
        else:
          return True
      return False
    
s = Solution()
print(s.increasingTriplet([1,2,3,4,5]), True)
print(s.increasingTriplet([5,4,3,2,1]), False)
print(s.increasingTriplet([2,1,5,0,4,6]), True)
print(s.increasingTriplet([20,100,10,12,5,13]), True)
print(s.increasingTriplet([2,4,-2,-3]), False)