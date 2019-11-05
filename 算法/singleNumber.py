#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   singleNumber.py
@Time    :   2019/11/05 22:21:02
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        hash表方法
        时间复杂度： O(n \cdot 1) = O(n)O(n⋅1)=O(n) 。for 循环的时间复杂度是 O(n)O(n) 的。
        Python 中哈希表的 pop 操作时间复杂度为O(1)O(1) 。
        空间复杂度： O(n)O(n) 。hash\_tablehash_table 需要的空间与 \text{nums}nums 中元素个数相等。
        144 ms	16.3 MB
        '''
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

    def singleNumber2(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
if __name__ == '__main__':
    pass