#2130 Maximum Twin Sum of a Linked List

class Solution:
    def pairSum(self, head):
        lis = []

        while head:
            lis.append(head.val)
            head = head.next

        return max(
            lis[i] + lis[-1 - i]
            for i in range(len(lis) // 2)
        )