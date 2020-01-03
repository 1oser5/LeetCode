#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   leastInterval.py
@Time    :   2019/12/30 16:04:16
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_d = {k:tasks.count(k) for k in sorted(tasks)}
        p = 0
        res = 0
        while sum(count_d.values()) != 0:
            for key in count_d:
                if count_d[key] != 0:
                    count_d[key] -= 1
                    p += 1
                    res += 1
                    if p >= n + 1:
                        p = 0
                        break
            else:
                while p < n + 1 and sum(count_d.values()) != 0:
                    p += 1
                    res += 1
                p = 0
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))