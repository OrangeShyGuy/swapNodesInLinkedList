class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next         
class Solution:
     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
         if not head:
           return head
         dummyNode = ListNode()
         previousNode = dummyNode
         currentNode = head
         if head.next == None:
           return head
         else:
           adjacentNode = currentNode.next
           while currentNode != None and currentNode.next != None:
             temp = adjacentNode.next
             previousNode.next = currentNode.next
             adjacentNode.next = currentNode
             currentNode.next = temp
             if temp != None:
                 previousNode = currentNode
                 currentNode = previousNode.next
                 adjacentNode = currentNode.next
         return dummyNode.next
