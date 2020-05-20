#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findTheLongestSubstring.py
@Time    :   2020/05/20 08:15:22
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ans, status, n = 0, 0, len(s)
        pos = [-1] * (1 << 5)  # 元音有5个，每个元音有奇偶俩种情况，所以所有情况为 32 中 2**5，下标为 10000 则表示 i 为奇数
        pos[0] = 0   # 默认为长度为0

        for i in range(n):
            if s[i] == 'a':
                status ^= 1 << 0
            elif s[i] == 'e':
                status ^= 1 << 1
            elif s[i] == 'i':
                status ^= 1 << 2
            elif s[i] == 'o':
                status ^= 1 << 3
            elif s[i] == 'u':
                status ^= 1 << 4
            if pos[status] != -1:  # 偶数个元音，可能的情况有俩种，奇数-奇数和偶数-偶数，所有如果之前有过相同值，直接减去
                ans = max(ans, i + 1 - pos[status])
            else:
                pos[status] = i + 1
        return ans

if __name__ == '__main__':
    s = Solution()
    c = s.findTheLongestSubstring('eleetminicoworoep')
    print(c)