#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   getLeastNumbers.py
@Time    :   2020/04/16 17:02:20
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        def quick_sort(l, left, right):
            if left >= right:
                return
            low = left
            high = right
            p = l[left]
            while left < right:
                while left < right and l[right] >= p:
                    right -= 1
                l[left] = l[right]
                while left < right and l[left] <= p:
                    left += 1
                l[right] = l[left]
            l[left] = p
            if left == k:
                return l
            if left > k:
                quick_sort(l, low, left-1)
            if left < k:
                quick_sort(l, left+1, high)
            return l
        c = quick_sort(arr, 0, len(arr)-1)
        print(c)
        return c[:k]


if __name__ == '__main__':
    s = Solution()
    c = s.getLeastNumbers([4, 5, 1, 6, 2, 3, 6, 7, 8], 2)
    print(c)