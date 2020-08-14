# -*- encoding: utf-8 -*-
'''
@File    :   respace.py
@Time    :   2020/08/14 10:47:19
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        d = set(dictionary)
        length = len(sentence)
        dp = [0] * (length+1)
        for i in range(1, length+1):
            dp[i] = dp[i-1] + 1
            for j in range(i):
                if sentence[j:i] in d:
                    dp[i] = min(dp[i], dp[j])
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    s.respace(["looked","just","like","her","brother"], "jesslookedjustliketimherbrother")

