# -*- encoding: utf-8 -*-
'''
@File    :   findCheapestPrice.py
@Time    :   2020/09/08 09:37:02
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        def dfs(cur, cost, k, res):
            # 不存在情况和过大情况
            if k < 0 or cost >= res[0]:
                return
            if cur == dst and k >= 0:
                res[0] = cost
                return
            for x in dictionary[cur]:
                dfs(x[0], cost +
                    x[1], k - 1, res)
        from collections import defaultdict
        dictionary = defaultdict(list)
        for i in flights:
            dictionary[i[0]].append((i[1], i[2]))
        res = [float('inf')]
        dfs(src, 0, K+1, res)
        return res[0] if res[0] != float('inf') else -1

    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dp = [[float('inf')] * n for _ in range(K + 1)]

        for flight in flights:
            if flight[0] == src:
                dp[0][flight[1]] = flight[2]

        for k in range(K + 1):
            dp[k][src] = 0

        for k in range(1, K + 1):
            for flight in flights:
                if dp[k-1][flight[0]] != float('inf'):
                    dp[k][flight[1]] = min(
                        dp[k][flight[1]], dp[k-1][flight[0]] + flight[2])
        return dp[K][dst] if dp[K][dst] != float('inf') else -1


if __name__ == '__main__':
    s = Solution().findCheapestPrice(
        5,
        [[1, 2, 10], [2, 0, 7], [1, 3, 8], [4, 0, 10], [3, 4, 2], [4, 2, 10], [0, 3, 3], [3, 1, 6], [2, 4, 5]], 0, 4, 1)
    print(s)
