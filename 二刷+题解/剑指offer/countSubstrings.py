#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   countSubstrings.py
@Time    :   2020/05/09 09:17:02
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for j in range(n):
            for i in range(j):
                if s[i] == s[j]:
                    #长度为2情况
                    if j-i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
        res = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j] == True:
                    res += 1
        return res



if __name__ == '__main__':
    s = Solution()
    c = s.countSubstrings("fdsklf")
    print(c)
