# -*- encoding: utf-8 -*-
'''
@File    :   divingBoard.py
@Time    :   2020/08/12 11:04:49
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        if shorter == longer:
            return [shorter * k]
        res = [0] * (k + 1)
        for i in range(k + 1):
            res[i] = shorter * (k - i) + longer * i
        return res

if __name__ == '__main__':
    pass