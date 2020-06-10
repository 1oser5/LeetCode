#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   largestNumber.py
@Time    :   2020/06/10 15:11:07
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':
    s = Solution()
    s.largestNumber([3, 30, 34, 5, 9])
