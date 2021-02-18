# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/2/18 9:05 下午
# @file : 03-数组中重复的数字.py
# @software : PyCharm

'''
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

限制：

2 <= n <= 100000

'''

# 1。哈希方式
a = [2, 3, 1, 0, 2, 5, 3]


class Solution:
    def findRepeatNumber(self, nums: list) -> int:
        set_a = set()
        for i in nums:
            if i in set_a:
                return i
            set_a.add(i)
        return 0


print(Solution().findRepeatNumber(a))


# 2。原地交换
class Solution:
    def findRepeatNumber(self, nums: list) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


print(Solution().findRepeatNumber(a))
