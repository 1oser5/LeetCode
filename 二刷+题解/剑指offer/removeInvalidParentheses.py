#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   removeInvalidParentheses.py
@Time    :   2020/05/06 19:36:07
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-invalid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        level = {s}

        while level:
            res = []
            for s in level:
                if self.isValid(s):
                    res.append(s)
            if res:
                return res

            next_level = set()
            for s in level:
                for i in range(len(s)):
                    if s[i] in '()':
                        next_level.add(s[:i] + s[i+1:])
            level = next_level


    def isValid(self, s):
        count = 0
        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0
if __name__ == '__main__':
    s = Solution()
    c = s.removeInvalidParentheses('()())()')
    print(c)