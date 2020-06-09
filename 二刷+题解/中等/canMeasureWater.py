#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   canMeasureWater.py
@Time    :   2020/06/02 12:13:34
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        seen = set()
        while stack:
            cur_x, cur_y = stack.pop()
            if cur_x == z or cur_y == z or cur_x + cur_y == z:
                return True
            if (cur_x, cur_y) in seen:
                continue
            seen.add((cur_x, cur_y))
            # full
            stack.append((x, cur_y))
            stack.append((cur_x, y))
            # empty
            stack.append((0, cur_y))
            stack.append((cur_x, 0))
            # add to other
            stack.append((cur_x - min(cur_x, y - cur_y), cur_y + min(cur_x, y - cur_y)))
            stack.append((cur_x + min(cur_y, x - cur_x), cur_y - min(cur_y, x - cur_x)))
        return False

if __name__ == '__main__':
    s = Solution()
    c = s.canMeasureWater(3, 5, 4)
    print(c)