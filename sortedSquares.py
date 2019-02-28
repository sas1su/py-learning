class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A_square = [num*num for num in A]
        A_square.sort()
        return A_square

s = Solution()
A = [-4, -1, 0, 3, 10]
A = [-7,-3,2,3,11]
r = s.sortedSquares(A)
print(r)