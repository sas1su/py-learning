class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        for num in nums:
            if num == m:
                continue
            if num * 2 > m:
                return -1
        return nums.index(m)
        
s = Solution()
nums = [3, 6, 1, 0]
r = s.dominantIndex(nums)
print(r)