#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findContinuousSequence.py
@Time    :   2020/04/15 09:48:26
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        half = target//2
        res = []
        left = 1
        cur = 0
        for i in range(1, half+2):
            cur += i
            while cur > target:
                cur -= left
                left += 1
            if cur == target:
                res.append(list(range(left, i+1)))
        return res
if __name__ == '__main__':
    s = Solution()
    c = s.findContinuousSequence(9)
    print(c)