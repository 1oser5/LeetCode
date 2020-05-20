#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   topKFrequent.py
@Time    :   2020/05/20 19:22:43
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in Counter(nums).most_common(k)]


if __name__ == '__main__':
    s = Solution()
    c = s.topKFrequent([3,1,1,2,2,1], k=2)
    print(c)