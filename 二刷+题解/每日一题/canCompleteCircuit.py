# -*- encoding: utf-8 -*-
'''
@File    :   canCompleteCircuit.py
@Time    :   2020/09/08 11:01:18
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s, m = 0, 0
        for i in range(len(gas)):
            s += gas[i] - cost[i]
            # 记录最小值，可以为负数
            m = min(s, m)
        # 总起油量小于消耗量，肯定走不完
        if s < 0:
            return -1
        # 如果 m 已经大于 0，直接返回 0 为起点
        if m > 0:
            return 0
        # 从右往左遍历，找到能将最小值 > 0 的点
        for i in range(len(gas)-1, -1, -1):
            diff = gas[i] - cost[i]
            m += diff
            if m >= 0:
                return i
        return -1
if __name__ == '__main__':
    s = Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
    print(s)