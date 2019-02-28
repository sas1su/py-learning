class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[-1] != len(nums):
            return len(nums)
        if nums[0] != 0:
            return 0
        m = max(nums)
        print(m)
        for i in range(m):
            print(i)
            if i not in nums:
                return i

nums = [0,1,2,3]
ret = Solution().missingNumber(nums)
print(ret)