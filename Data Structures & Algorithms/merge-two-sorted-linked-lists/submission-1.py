# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        print(self.getList(list1,list2))

        newList = self.getList(list1,list2)

        newList.sort()

        if not newList:
            return None
        head = ListNode(newList[0])

        current = head

        for num in newList[1:]:
            current.next = ListNode(num)
            current = current.next
        return head

        
    
    def getList(self, head, head2):

        regularList = []
        node = head
        node2 = head2

        while node is not None:
            regularList.append(node.val)

            node = node.next

        while node2 is not None:
            regularList.append(node2.val)

            node2 = node2.next
        
        return regularList