"""
Given an array nums,
write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12],
after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

## NOTES
* use lambda cmp function and return -1 when the second value is non-zero
* this will help it move up the array
* dont care about preserving the value, just copy everything to the front
* fill the rest of the array with zeroes
"""
class Solution(object):
    def moveZeroesLambda(self, nums):
        return nums.sort(cmp= lambda a, b: -1 if b == 0 else 0)

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zi = 0
        for i in range(len(nums)):
            if(nums[zi] != 0):
                zi = self.findNextZeroIndex(nums, zi)
            if zi == len(nums):
                break
            if zi < i and nums[i] != 0:
                nums[zi] = nums[i]
                nums[i] = 0
        return nums

    def findNextZeroIndex(self, nums, pos):
        for i in range(pos, len(nums)):
            if(nums[i] == 0):
                return i
        return len(nums)
        
if __name__ == '__main__':
    sol = Solution()
    print sol.findNextZeroIndex([0, 1, 0, 3, 12, 10, 6], 6)
    print sol.moveZeroes([0, 1, 0, 3, 12])
    print sol.moveZeroesLambda([0, 1, 0, 3, 12])
    print sol.moveZeroes([1, 0, 3, 0, 12])
    print sol.moveZeroes([1, 3, 0, 12, 0])
    print sol.moveZeroes([1, 3, 12, 0, 0])
    print sol.moveZeroes([0, 0, 0, 0, 0])
    print sol.moveZeroes([1, 1, 1, 1, 1])
    print sol.moveZeroes([])
    print sol.moveZeroes([0])
    print sol.moveZeroes([1])
