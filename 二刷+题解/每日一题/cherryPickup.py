# -*- encoding: utf-8 -*-
'''
@File    :   cherryPickup.py
@Time    :   2020/09/14 09:35:10
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = []
        for i in range(n + 1):
            dp.append([])
            for j in range(n + 1):
                dp[i].append([])
                for _ in range(n + 1):
                    dp[i][j].append(-1)
        dp[1][1][1] = grid[0][0]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for k in range(1, min(i + j + 1, n + 1)):
                    # i + j = l + k ,俩人步长一致
                    l = i + j - k
                    # 跳过非法情况
                    if not 1 <= l <= n or grid[i-1][j-1] == -1 or grid[k-1][l-1] == -1:
                        continue
                    ans = max(
                        dp[i-1][j][k],
                        dp[i][j-1][k],
                        dp[i-1][j][k-1],
                        dp[i][j-1][k-1]
                    )
                    if ans < 0:
                        continue
                    ans += grid[i-1][j-1] + (grid[k-1][l-1] if k != i and l != j else 0)   # 注意判断是否在同一个点上,必须加括号，给这个括号坑惨了
                    dp[i][j][k] = ans
        return dp[-1][-1][-1] if dp[-1][-1][-1] > 0 else 0
if __name__ == '__main__':
    s = Solution()
    c = s.cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]])
    print(c)