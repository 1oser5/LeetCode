#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   fourSum.py
@Time    :   2020/04/13 12:46:32
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if len(nums) < 4:
            return []
        nums = sorted(nums)
        for index, val in enumerate(nums[:-2]):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            q = target - val
            new_n = nums[index+1:]
            # 如果 3 * 最大数 < q:
            if 3 * new_n[-1] < q:
                continue
            for i, k in enumerate(new_n):
                if i > 0 and new_n[i] == new_n[i-1]:
                    continue
                # 如果 3*k > q，表示后面不可能存在 == q 情况
                if 3 * k > q:
                    break
                start = i + 1
                end = len(new_n) - 1
                while start < end:
                    s = k + new_n[start] + new_n[end]
                    if s < q:
                        start += 1
                    elif s > q:
                        end -= 1
                    else:
                        res.append([val, k, new_n[start], new_n[end]])
                        start += 1
                        end -= 1
                        while start < end and new_n[start] == new_n[start-1]:
                            start += 1
                        while start < end and new_n[end] == new_n[end+1]:
                            end -= 1
        return res

if __name__ == '__main__':
    s = Solution()
    c = s.fourSum([1,-2,-5,-4,-3,3,3,5], -11)
    print(c)