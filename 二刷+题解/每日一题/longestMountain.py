#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   longestMountain.py
@Time    :   2020/05/20 15:22:04
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：

B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。

如果不含有 “山脉” 则返回 0。

 

示例 1：

输入：[2,1,4,7,3,2,5]
输出：5
解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
示例 2：

输入：[2,2,2]
输出：0
解释：不含 “山脉”。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-mountain-in-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res = 0
        for i in range(1, len(A) - 1):
            left, right = i-1, i+1
            if A[left] < A[i] and A[i] > A[right]:
                while left-1 >= 0 and A[left] > A[left-1]:
                    left -= 1
                while right+1 <= len(A)-1 and A[right] > A[right+1]:
                    right += 1
                res = max(res, right-left+1)
        return res


if __name__ == '__main__':
    s = Solution()
    c = s.longestMountain([0,1,2,3,4,5,6,7,8,9])
    print(c)
