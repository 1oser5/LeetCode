#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   evalRPN.py
@Time    :   2020/05/22 17:23:30
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6
示例 3：

输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ''' 使用 eval '''
        import math
        calculation = {'*', '+', '-', '/'}
        stack = []
        res = 0
        for token in tokens:
            if token in calculation:
                b, a = stack.pop(), stack.pop()
                res = eval(a + ' ' + token + ' ' + b)
                res = math.ceil(res) if res < 0 else math.floor(res) # 正数向下取整，负数向上取整
                stack.append(str(res))
            else:
                stack.append(token)
        if stack:
            return int(stack.pop())
        return res

    def evalRPN2(self, tokens: List[str]) -> int:
        ''' 使用 opt 操作符 '''
        stack = []
        plus = lambda a, b : b + a
        sub = lambda a, b: b - a
        mul = lambda a, b: b * a
        div = lambda a, b: int(b / a)
        opt = {
            "+": plus,
            "-": sub,
            "*": mul,
            "/": div
        }
        for t in tokens:
            if t in opt:
                stack.append(opt[t](stack.pop(), stack.pop()))
            else:
                stack.append(int(t))
        return stack.pop()
if __name__ == '__main__':
    s = Solution()
    #c = s.evalRPN(["2", "1", "+", "3", "*"])
    #c = s.evalRPN(["4", "13", "5", "/", "+"])
    c = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print(c)