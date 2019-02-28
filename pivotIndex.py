class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1

        
s = Solution()
nums = [1, 7, 3, 7, 5, 6, 6, 6]
r = s.pivotIndex(nums)
print(r)