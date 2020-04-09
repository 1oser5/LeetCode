#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   generateParenthesis.py
@Time    :   2020/04/09 11:04:37
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：

输入：n = 3
输出：[
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
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(s, left, right):
            if left == 0 and right == 0:
                res.append(s)
                return
            if left > right:
                return
            if left > 0:
                helper(s+'(', left-1, right)
            if right > 0:
                helper(s+')', left, right-1)
        helper('', n, n)
        return res
if __name__ == '__main__':
    s = Solution()
    c = s.generateParenthesis(3)
    print(c)