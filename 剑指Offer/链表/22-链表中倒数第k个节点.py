# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/2/22 9:40 下午
# @file : 22-链表中倒数第k个节点.py
# @software : PyCharm

'''
输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有 6 个节点，从头节点开始，
它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

示例：
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p_head=head
        n=1
        while p_head:
            n+=1
            p_head=p_head.next

        for i in range(n-k-1):
            head=head.next
        return head

class Solution2(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p_fast=head
        p_slow=head
        for i in range(k):
            p_fast=p_fast.next
        while p_fast:
            p_fast=p_fast.next
            p_slow=p_slow.next
        return p_slow
