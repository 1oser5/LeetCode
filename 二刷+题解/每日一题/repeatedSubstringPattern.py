# -*- encoding: utf-8 -*-
'''
@File    :   repeatedSubstringPattern.py
@Time    :   2020/08/25 08:17:05
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]

if __name__ == '__main__':
    pass