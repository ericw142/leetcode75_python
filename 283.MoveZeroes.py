# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]

 

# Constraints:

#     1 <= nums.length <= 104
#     -231 <= nums[i] <= 231 - 1

 
# Follow up: Could you minimize the total number of operations done?


class Solution(object):
    def moveZeroes(self, nums):
        insert_pos = 0
        
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1

nums = [0,1,0,3,12]

myclass = Solution()
myclass.moveZeroes(nums)
print(nums)