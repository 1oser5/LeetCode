#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   subarraySum.py
@Time    :   2020/05/15 08:11:54
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        num_count = defaultdict(int)
        num_count[0] = 1
        cur = 0
        res = 0
        n = len(nums)
        for i in range(n):
            cur += nums[i]
            if cur - k in num_count:
                res += num_count[cur-k]
            num_count[cur] += 1
        return res
if __name__ == '__main__':
    s = Solution()
    c = s.subarraySum([1,1,1], 2)
    print(c)