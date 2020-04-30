#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   isHappy.py
@Time    :   2020/04/30 08:36:10
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

 

示例：

输入：19
输出：true
解释：


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def isHappy(self, n: int) -> bool:
        """ 集合解法 """
        s = set()

        def helper(n, s):
            if n == 1:
                return True
            if n in s:
                return False
            l = list(str(n))
            res = 0
            for i in range(len(l)):
                res += pow(int(l[i]), 2)
            s.add(n)
            return helper(res, s)
        return helper(n, s)


    def isHappy1(self, n: int) -> bool:
        """ 快慢指针 """
        n = str(n)
        slow = n
        fast = str(sum(int(i) ** 2 for i in n))
        while slow != fast:
            slow = str(sum(int(i) ** 2 for i in slow))
            fast = str(sum(int(i) ** 2 for i in fast))
            fast = str(sum(int(i) ** 2 for i in fast))
        return slow == "1"




if __name__ == '__main__':
    s = Solution()
    c = s.isHappy(19)
    print(c)