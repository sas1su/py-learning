class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        newdigit = int(''.join([str(x) for x in digits]))+1
        return [int(x) for x in str(newdigit)]


s = Solution()
digits = [1, 2, 3]
r = s.plusOne(digits)
print(r)