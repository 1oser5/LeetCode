#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   canJump.py
@Time    :   2020/04/17 08:38:28
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """ case 24 超时 """
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(n):
            if dp[i]:
                j = i+1
                while j < n and j < i + nums[i] + 1:
                    dp[j] = True
                    j += 1
            if not dp[i]:
                return False
        return dp[-1]

    def canJump1(self, nums: List[int]) -> bool:
        n, most = len(nums), 0
        for i in range(n):
            if i > most:
                return False
            most = max(most, nums[i] + i)
            if most >= n - 1:
                return True
        return False





if __name__ == '__main__':
    s = Solution()
    c = s.canJump1([2,3,1,1,4])
    print(c)