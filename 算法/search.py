#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   search.py
@Time    :   2019/12/01 12:28:12
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def search(self, nums: [int], target: int) -> int:
        def find_rotateindex(l,r):
            if(nums[l]<nums[r]):
                return 0
            while(l<=r):
                rotate=(l+r)//2
                if(nums[rotate]<nums[rotate-1]):
                    return rotate
                
                if(nums[rotate]>nums[r]):
                    l=rotate+1
                else:
                    r=rotate-1
        #print(find_rotateindex(0,len(nums)-1))
        def find(l,r):
            while(l<=r):
                mid=(l+r)//2
                if(nums[mid]==target):
                    return mid
                if(nums[mid]>target):
                    r=mid-1
                else:
                    l=mid+1
            return -1
        n=len(nums)
        if(n==0):
            return -1
        if(n==1):
            return 0 if(nums[0]==target) else -1
        rotateindex=find_rotateindex(0,n-1)
        if(rotateindex==0):
            return find(0,n-1)
            
        if(target>=nums[0]):
            return find(0,rotateindex)
        else:
            return find(rotateindex,n-1)

      
            
if __name__ == '__main__':
    pass