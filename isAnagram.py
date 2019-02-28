class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        m1 = collections.Counter(s)
        m2 = collections.Counter(t)
        for k in m1.keys():
            if m1[k] != m2[k]:
                return False
        return True

import collections     
s = "anagras"
t = "nagaram"
ret = Solution().isAnagram(s, t)
# should be true or false
print(ret)