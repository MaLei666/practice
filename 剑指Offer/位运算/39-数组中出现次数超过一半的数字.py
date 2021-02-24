#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/2/23 9:52 下午
# @file : 39-数组中出现次数超过一半的数字.py
# @software : PyCharm

'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

限制：
1 <= 数组长度 <= 50000
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        dict_nums=dict.fromkeys(nums,0)
        half=len(nums)/2
        for i in nums:
            dict_nums[i]+=1
            if dict_nums[i]>half:
                return i