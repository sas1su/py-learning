class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        for i, v in enumerate(s):
            if v in m:
                m[v] = m[v] + 1
            else:
                m[v] = 1
        print(m)
        for i in range(len(s)):
            if m[s[i]] == 1:
                return i
        return -1

s = "loveleetcode"
ret = Solution().firstUniqChar(s)
print(ret)