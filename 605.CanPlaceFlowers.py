# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

 

# Constraints:

#     1 <= flowerbed.length <= 2 * 104
#     flowerbed[i] is 0 or 1.
#     There are no two adjacent flowers in flowerbed.
#     0 <= n <= flowerbed.length


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        totalThatCanBePlanted = 0

        for idx, plot in enumerate(flowerbed):
            if totalThatCanBePlanted >= n:
                break
            elif plot == 1:
                continue
            else:
                if (idx == 0 or flowerbed[idx-1] == 0) and (idx+1 >= len(flowerbed) or flowerbed[idx+1] == 0):
                    totalThatCanBePlanted+= 1
                    flowerbed[idx] = 1
        
        if totalThatCanBePlanted >= n:
            return True
        else:
            return False
        

flowerbed = [1,0,0,0,1,0,0]
n = 2

myclass = Solution()
answer = myclass.canPlaceFlowers(flowerbed, n)
print(answer)