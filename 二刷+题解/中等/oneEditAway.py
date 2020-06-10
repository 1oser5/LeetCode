#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   oneEditAway.py
@Time    :   2020/06/10 15:54:13
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m = len(first)
        n = len(second)
        if abs(m - n) > 1:
            return False
        for i in range(min(m, n)):
            if first[i] == second[i]:
                pass
            else:
                return first[i+1:] == second[i+1:] or first[i:] == second[i+1:] or first[i+1:] == second[i:]
        return True


if __name__ == '__main__':
    pass
