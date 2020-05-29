#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   decodeString.py
@Time    :   2020/05/28 19:15:17
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, mutli = [], '', 0
        for c in s:
            if c == '[':
                stack.append((mutli, res))
                res, mutli = '', 0
            elif c == ']':
                cur_mutli, last_res = stack.pop()
                res = last_res + cur_mutli * res
            elif '0' <= c <= '9':  # smart way
                mutli = 10 * mutli + int(c)
            else:
                res += c
        return res



if __name__ == '__main__':
    s = Solution()
    c = s.decodeString('3[a]2[bc]')
    print(c)