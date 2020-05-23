#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   minWindow.py
@Time    :   2020/05/23 09:04:43
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        res = s
        size = len(s)
        t_counter = Counter(t)
        c_counter = Counter()
        left = 0
        for i in range(size):
            if s[i] in t:
                c_counter[s[i]] += 1
            while c_counter[s[i]] > t_counter[s[i]]:
                if s[left] in t:
                    c_counter[s[left]] -= 1
                left += 1
                while s[left] not in t and left < i:
                    left += 1
            if sum(c_counter.values()) >= sum(t_counter.values()):
                res = res if len(res) < len(s[left:i+1]) else s[left:i+1]
        return res

    def minWindow2(self, s: str, t: str) -> str:
        ''' 这人的去多余比我做的好 '''
        from collections import Counter
        t = Counter(t)
        lookup = Counter()
        start = 0
        end = 0
        min_len = float("inf")
        res = ""
        while end < len(s):
            lookup[s[end]] += 1
            end += 1
            #print(start, end)
            while all(map(lambda x: lookup[x] >= t[x], t.keys())):
                if end - start < min_len:
                    res = s[start:end]
                    min_len = end - start
                lookup[s[start]] -= 1
                start += 1
        return res

if __name__ == '__main__':
    s = Solution()
    c = s.minWindow("ADOBECODEBANC", "ABC")
    print(c)