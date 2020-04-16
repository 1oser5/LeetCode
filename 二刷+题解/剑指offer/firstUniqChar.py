#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   firstUniqChar.py
@Time    :   2020/04/16 16:45:01
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def firstUniqChar(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = not i in d
        for k, v in d.items():
            if v:
                return k
        return ' '
if __name__ == '__main__':
    pass