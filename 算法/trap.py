#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   trap.py
@Time    :   2019/12/17 15:56:43
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        cur = 0
        res = 0
        low_stack = []
        high_stack = []
        while cur < len(height) - 1:
            while cur < len(height) - 1 and height[cur] > height[cur+1]:
                low_stack.append(height[cur])
                cur += 1
            while  cur < len(height) - 1 and height[cur] < height[cur+1] and low_stack:
                #存储最低点
                if not high_stack:
                    high_stack.append(height[cur])
                high_stack.append(height[cur+1])
                cur += 1
            if high_stack and low_stack:
                while high_stack[-1] < low_stack[0] and len(low_stack) > 1:
                    low_stack.pop(0)
                res += min(low_stack[0], high_stack[-1]) * (len(high_stack)+len(low_stack)-2) - sum(high_stack[:-1]) - sum(low_stack[1:])
                low_stack,high_stack = [],[]
                continue
            cur += 1
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))