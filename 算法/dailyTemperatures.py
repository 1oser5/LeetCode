#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   dailyTemperatures.py
@Time    :   2019/10/18 07:55:58
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0
 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
def dailyTemperatures(T):
    '''
    568 ms	17.5 MB
    通过维护一个递减栈来实现效率提升
    '''
    stack = list()
    length = len(T)
    result = [0] * length
    for key, value in enumerate(T):
        if stack:
            while stack and T[stack[-1]] < value:
                result[stack[-1]] = key - stack[-1]
                stack.pop()
        stack.append(key)
    return result
if __name__ == '__main__':
    print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))