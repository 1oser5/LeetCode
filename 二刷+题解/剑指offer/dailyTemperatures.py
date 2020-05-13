#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   dailyTemperatures.py
@Time    :   2020/05/13 21:34:08
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return
        n = len(T)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and T[stack[-1]] < T[i]:
                prev = stack.pop()
                res[prev] = i-prev
            stack.append(i)
        return res
if __name__ == '__main__':
    s = Solution()
    c = s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(c)