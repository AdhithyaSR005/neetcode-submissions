# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        arr=[]
        while curr:
            arr.append(curr)
            curr=curr.next

        a=len(arr)
        k=len(arr)-n
        if k == 0:
            return head.next

        # Skip the node
        arr[k - 1].next = arr[k].next

        return head

    

        