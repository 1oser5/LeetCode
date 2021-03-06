#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   nthUglyNumber.py
@Time    :   2020/04/23 17:11:03
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chou-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        a, b, c = 0, 0, 0
        for i in range(1, n):
            n1 = dp[a] * 2
            n2 = dp[b] * 3
            n3 = dp[c] * 5
            dp[i] = min(n1, n2, n3)
            if dp[i] == n1:
                a += 1
            if dp[i] == n2:
                b += 1
            if dp[i] == n3:
                c += 1
        return dp[-1]
if __name__ == '__main__':
    pass