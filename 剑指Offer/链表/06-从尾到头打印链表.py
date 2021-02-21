# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/2/21 9:38 下午
# @file : 06-从尾到头打印链表.py
# @software : PyCharm

'''
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 栈
class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        list_a = []
        while head:
            list_a.append(head.val)
            head = head.next
        return list_a[::-1]

# 递归
class Solution2(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        return self.reversePrint(head.next)+[head.val] if head else []