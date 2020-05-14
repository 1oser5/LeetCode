#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   longestValidParentheses.py
@Time    :   2020/05/14 09:52:23
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ''' 超时 '''
        level = {s}
        res = 0
        memory = set()
        while level:
            for c in level:
                if c and self.isValid(c):
                    res = max(res, len(c))

            next_level = set()
            for c in level:
                if c in memory:
                    continue
                memory.add(c)
                for i in range(len(c)):
                    next_level.add(c[:i])
                    next_level.add(c[i+1:])
            level = next_level
        return res



    def isValid(self, s):
        count = 0
        for i in s:
            if i == '(':
                count += 1
            elif i == ')' and count > 0:
                count -= 1
            else:
                return False
        return count == 0

    def longestValidParentheses1(self, s: str) -> int:
        """ 天秀栈 """
        if not s:
            return 0
        stack = [-1]  # 神之一手
        n = len(s)
        res = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # 保护
                else:
                    res = max(res, i - stack[-1])
        return res

    def longestValidParentheses2(self, s: str) -> int:
        """ 地秀动态规划 """
        if not s:
            return 0
        res = 0
        n = len(s)
        dp = [0] * n  # dp[i] 表示以 i 结尾的有效括号长度
        for i in range(1, n):  # 从1开始没毛病，括号至少要俩个字符
            if s[i] == ')':  # 以 ( 结尾的肯定不有效，直接忽略
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                if s[i-1] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':  # i-dp[i-1]-1 表示上一个不匹配的字符
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2  # 这里把之前匹配和不匹配的连接起来了
                res = max(res, dp[i])
        return res


if __name__ == '__main__':
    s = Solution()
    c = s.longestValidParentheses2(")()())")
    print(c)