# -*- encoding: utf-8 -*-
'''
@File    :   longestValidParentheses.py
@Time    :   2020/08/12 08:36:08
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    # 写复杂了
    def longestValidParentheses(self, s: str) -> int:
        size = len(s)
        dp = [0] * size
        res = 0
        for i in range(1, size):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                if s[i-1] == ')' and i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i - dp[i - 1] - 2]
                res = max(res, dp[i])
        return res
if __name__ == '__main__':
    s = Solution()
    c = s.longestValidParentheses1("()(()")
    print(c)