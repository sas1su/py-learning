class Solution:
    def isValid(self, s: 'str') -> 'bool':
        try:
            sTmp=[]
            for i in s:
                #print("i="+i)
                #print("sTmp="+sTmp)
                if i=="(":
                    sTmp.append(")")
                elif i=="{":
                    sTmp.append("}")
                elif i=="[":
                    sTmp.append("]")
                elif i==")":
                    if sTmp.pop()!=")":
                        return False
                elif i=="}":
                    if sTmp.pop()!="}":
                        return False
                elif i=="]":
                    if sTmp.pop()!="]":
                        return False
                else:
                    return False
            return len(sTmp)==0
        except:
            return False
        

s = ']'
ret = Solution().isValid(s)
print(ret)