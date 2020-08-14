# -*- encoding: utf-8 -*-
'''
@File    :   isValid.py
@Time    :   2020/08/14 08:22:10
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def isValid(self, s: str) -> bool:
        memory = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for v in s:
            if v in ['(', '{', '[']:
                stack.append(memory[v])
            else:
                if not stack or stack.pop() != v:
                    return False
        return not stack

    pass