#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   mySqrt.py
@Time    :   2020/05/09 08:36:52
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = 999999
        while left < right:
            # 这种取中位数的方法又快又好，是我刚学会的，原因在下面这篇文章的评论区
            # https://www.liwei.party/2019/06/17/leetcode-solution-new/search-insert-position/
            mid = (left + right + 1) >> 1
            square = mid * mid
            if square > x:
                right = mid - 1
            else:
                left = mid

        return left


if __name__ == '__main__':
    s = Solution()
    c = s.mySqrt(4)
    c = s.mySqrt(1908934429)