#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   isStraight.py
@Time    :   2020/04/23 11:00:37
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        else_zero_l = [x for x in nums if x != 0]
        return max(else_zero_l) - min(else_zero_l) <= 4 and len(else_zero_l) == len(set(else_zero_l))

    def isStraight1(self, nums: List[int]) -> bool:
        repeat = set()
        _max = 0
        _min = 14
        for num in nums:
            if num == 0:
                continue
            _max = max(_max, num)
            _min = min(_min, num)
            if num in repeat:
                return False
            repeat.add(num)
        return _max - _min < 5

if __name__ == '__main__':
    pass