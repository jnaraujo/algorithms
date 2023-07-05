class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pos = 0
        for index, num in enumerate(nums):
            if num != 0:
                if pos != index:
                  nums[pos], nums[index] = nums[index], nums[pos]
                pos += 1

s = Solution()
print(s.moveZeroes([0,1,0,3,12]), [1,3,12,0,0])
print(s.moveZeroes([0]), [0])
print(s.moveZeroes([0, 2, 0, 0, 15, 4, 45, 0, 0, 1, 0]))