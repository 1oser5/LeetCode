#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   maxArea.py
@Time    :   2020/04/12 15:34:16
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        m = 0
        while start < end:
            if height[start] > height[end]:
                m = max(m, height[end] * (end - start))
                end -= 1
            else:
                m = max(m, height[start] * (end - start))
                start += 1
        return m
if __name__ == '__main__':
    s = Solution()
    c = s.maxArea([1,8,6,2,5,4,8,3,7])
    print(c)