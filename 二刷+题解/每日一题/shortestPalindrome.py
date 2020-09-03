# -*- encoding: utf-8 -*-
'''
@File    :   shortestPalindrome.py
@Time    :   2020/09/03 14:02:45
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        ''' 超时解法 '''
        if not s:
            return ''
        res = s
        # 保证length永远为奇数
        s = '#' + '#'.join(list(s)) + '#'
        length = len(s)
        # 中部
        mid = length // 2
        for i in range(mid, -1, -1):
            left = i - 1
            right = i + 1
            flag = True
            while left >= 0 and right < length and flag:
                if s[left] != s[right]:
                    flag = False
                left -= 1
                right += 1
            if left < 0:
                res = ''.join(s[right:][::-1].split('#')) + res
                return res


    def shortestPalindrom1e(self, s: str) -> str:
        ''' kmp 永远滴神 '''
        def get_table(p):
            table = [0] * len(p)
            i = 1
            j = 0
            while i < len(p):
                if p[i] == p[j]:
                    j += 1
                    table[i] = j
                    i += 1
                else:
                    if j > 0:
                        j = table[j - 1]
                    else:
                        i += 1
                        j = 0
            return table

        table = get_table(s + "#" + s[::-1])
        print(table)
        return s[table[-1]:][::-1] + s

if __name__ == '__main__':
    s = Solution()
    c = s.shortestPalindrom1e("aacecaaa")
    print(c)