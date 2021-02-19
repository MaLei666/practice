# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/2/19 9:22 下午
# @file : 50-第一个只出现一次的字符.py
# @software : PyCharm
'''
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "

限制：

0 <= s 的长度 <= 50000
'''

# 有序字典
from collections import OrderedDict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict1 = OrderedDict()
        for i in s:
            if not dict1.get(i):
                dict1.setdefault(i, 1)
            else:
                dict1[i] += 1
        for i, j in dict1.items():
            if j == 1:
                return i
        return ' '


# 布尔值
class Solution2(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict1 = dict()
        for i in s:
            dict1[i] = not i in dict1
        for j in s:
            if dict1[j]:
                return j
        return ' '


s = "abaccdeff"
print(Solution2().firstUniqChar(s))
