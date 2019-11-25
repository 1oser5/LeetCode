#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   generateParenthesis.py
@Time    :   2019/11/25 21:10:20
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        res = []
        def foo(a, b, c):
            '''52 ms	13.9 MB'''
            if b<0 or c<0: return
            if b == c == 0: res.append(a)
            if b< c:
                foo(a + '(',b-1,c)
                foo(a + ')',b,c-1)
        foo('',n,n)
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))