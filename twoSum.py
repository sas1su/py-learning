class Solution(object):
    def twoSum(self, nums, target):
        """
        iterate the array
        make the hash table
        lookup the hashtable
        """
        seen = {}
        for num in nums:
            compliment = target - num
            if compliment in seen.keys():
                return [seen[compliment], nums.index(num)]
            else:
                seen[num] = nums.index(num)  


s = Solution()

nums = [1, 2, 11, 7]
target = 9
r = s.twoSum(nums, target)
print(r)