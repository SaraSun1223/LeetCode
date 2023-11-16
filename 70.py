# 70. 爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# 提示 0 < n <= 45

# 1 递归
class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 1 or n == 2):
            return n

        # return climbStairs(n-1)+climbStairs(n-2) python不能这样写
        a = 1
        b = 2
        temp = 0
        for i in range(3, n + 1):
            temp = a + b
            a = b
            b = temp
        return temp


