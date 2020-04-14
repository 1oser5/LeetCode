#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   uniquePaths.py
@Time    :   2020/04/13 19:51:37
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (m+1) for _ in range(n+1)]
        dp[0][1] = 1
        for col in range(1, n+1):
            for raw in range(1, m+1):
                dp[col][raw] = dp[col-1][raw] + dp[col][raw-1]
        return dp[-1][-1]

    def uniquePaths1(self, m,n):
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]

if __name__ == '__main__':
    s = Solution()
    s.uniquePaths1(7,3)