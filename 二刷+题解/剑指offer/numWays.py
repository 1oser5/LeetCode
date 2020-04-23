#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   numWays.py
@Time    :   2020/04/23 11:11:17
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def numWays(self, n: int) -> int:
        prev, cur = 1, 1
        for _ in range(n):
            prev, cur = cur, prev + cur
        return prev % 1000000007
        # a, b = 1, 1
        # for _ in range(n):
        #     a, b = b, a + b
        # return a % 1000000007


if __name__ == '__main__':
    s = Solution()
    c = s.numWays(11)
    print(c)