#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   movingCount.py
@Time    :   2020/04/08 09:31:02
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 1：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        """ 递归 巨慢无比"""
        memory = []

        def add_coor(a, b):
            ans = 0
            while a != 0:
                ans += a % 10
                a //= 10
            while b != 0:
                ans += b % 10
                b //= 10
            return ans

        def __dfs(col, row):
            if col >= m or row >= n:
                return
            # 减少递归
            if [col, row] in memory:
                return
            if add_coor(col, row) <= k:
                memory.append([col, row])
                __dfs(col+1, row)
                __dfs(col, row+1)
        __dfs(0, 0)
        return len(memory)

    def movingCount1(self, m: int, n: int, k: int) -> int:
        """ 比递归快了十倍 """
        res = [(0, 0)]

        def add_coor(a, b):
            ans = 0
            while a != 0:
                ans += a % 10
                a //= 10
            while b != 0:
                ans += b % 10
                b //= 10
            return ans
        for col in range(m):
            for row in range(n):
                if add_coor(col, row) <= k and ((col-1, row) in res or (col, row-1) in res):
                    res.append((col, row))
        return len(res)




if __name__ == '__main__':
    s = Solution()
    #c = s.movingCount(16,8,4)
    c = s.movingCount1(3,2,17)
    print(c)
