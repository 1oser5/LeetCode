#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   fourSumCount.py
@Time    :   2020/04/13 13:47:43
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List
import profile

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """ 20 case timeout """
        res = []
        memory = set()
        if not (A and B and C and D):
            return len(res)
        A = sorted(A)
        B = sorted(B)
        C = sorted(C)
        D = sorted(D)
        start = 0
        end = len(A) - 1

        def helper(a, b, c, d):
            if (a, b, c, d) in memory:
                return
            else:
                memory.add((a, b, c, d))
            t = A[a] + B[b] + C[c] + D[d]
            if t == 0:
                res.append((a, b, c, d))
            if t < 0:
                return
            if a > start:
                helper(a-1, b, c, d)
            if b > start:
                helper(a, b-1, c, d)
            if c > start:
                helper(a, b, c-1, d)
            if d > start:
                helper(a, b, c, d-1)
        helper(end, end, end, end)
        return len(res)

    def fourSumCount1(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """ 24 case timeout """
        res = [0]
        if not (A and B and C and D):
            return res[0]
        memeroy = set()

        def counter(l, d):
            for i in l:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
            return d
        A_dict = counter(A, {})
        B_dict = counter(B, {})
        C_dict = counter(C, {})
        D_dict = counter(D, {})
        A_key = sorted(list(A_dict.keys()))
        B_key = sorted(list(B_dict.keys()))
        C_key = sorted(list(C_dict.keys()))
        D_key = sorted(list(D_dict.keys()))

        def helper(a, b, c, d):
            if (a, b, c, d) in memeroy:
                return
            else:
                memeroy.add((a, b, c, d))
            t = A_key[a] + B_key[b] + C_key[c] + D_key[d]
            if t == 0:
                res[-1] += A_dict[A_key[a]] * B_dict[B_key[b]] * C_dict[C_key[c]] * D_dict[D_key[d]]
            if t > 0:
                return
            if a < len(A_key) - 1:
                helper(a+1, b, c, d)
            if b < len(B_key) - 1:
                helper(a, b+1, c, d)
            if c < len(C_key) - 1:
                helper(a, b, c+1, d)
            if d < len(D_key) - 1:
                helper(a, b, c, d+1)
        helper(0, 0, 0, 0)
        return res[-1]


def fourSumCount2(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    import collections
    lookup = collections.defaultdict(int)
    res = 0
    for a in A:
        for b in B:
            lookup[a+b] += 1
    for c in C:
        for d in D:
            res += lookup[-(c + d)]
    return res

if __name__ == '__main__':
    s = Solution()
    #print(c)


