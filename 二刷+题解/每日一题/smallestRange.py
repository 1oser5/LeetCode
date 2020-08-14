# -*- encoding: utf-8 -*-
'''
@File    :   smallestRange.py
@Time    :   2020/08/14 08:47:45
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    # sliding windows
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        size = len(nums)
        total = []
        for i in range(size):
            for j in range(len(nums[i])):
                total.append((nums[i][j], i))
        total = sorted(total, key=lambda x: x[0])
        left, right = -10**9, 10**9
        from collections import Counter
        counter = Counter()
        j = 0
        for i in range(len(total)):
            counter[total[i][1]] += 1
            if len(counter) == size:
                while counter[total[j][1]] > 1:
                    counter[total[j][1]] -= 1
                    j += 1
                if right - left > total[i][0] - total[j][0]:
                    left, right = total[j][0], total[i][0]
        return [left, right]

if __name__ == '__main__':
    s = Solution()
    c = s.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])
    print(c)