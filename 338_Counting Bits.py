# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

# 示例 1:

# 输入: 2
# 输出: [0,1,1]
#复杂度O(n)下，只战胜27%

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        list = []
        for i in range(0,num+1):
            a = bin(i)
            list.append(a.count('1'))
        return list
s = Solution()
num = int(input())
print(s.countBits(num))