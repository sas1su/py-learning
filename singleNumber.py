class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for i in nums:
            try:
                m.pop(i)
            except:
                m[i] = 1
        return m.popitem()[0]

nums = [2, 1, 2]   
#nums = [4,1,2,1,2]     
ret = Solution().singleNumber(nums)
print(ret)