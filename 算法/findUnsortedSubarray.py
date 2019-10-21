#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findUnsortedSubarray.py
@Time    :   2019/10/21 13:45:46
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路
排序前后的位置差异来确定长度
'''
# here put the import lib
# def findUnsortedSubarray(nums):
#     '''260 ms	15.2 MB'''
#     l = sorted(nums)
#     length = len(nums)
#     start = 0
#     end = -1
#     for x in range(length):
#         if nums[x] != l[x]:
#             start = x
#             break
#     for x in range(length-1,0,-1):
#         if nums[x] != l[x]:
#             end = x
#             break
#     return end - start + 1

'''参考后修改答案'''
def findUnsortedSubarray(nums):
    sorted_nums = sorted(nums)
    p1 = 0
    p2 = len(nums) - 1
    while p1 <= p2 and sorted_nums[p1] == nums[p1]:
        p1 += 1
    while p1 <= p2 and sorted_nums[p2] == nums[p2]:
        p2 -= 1
    return p2 - p1 + 1
if __name__ == '__main__':
    print(findUnsortedSubarray([1,2,3,4]))