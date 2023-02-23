#Iteration
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        #while loop, looping thru both lists
        while list1 and list2:
            #if the current head is less than the head of list 2, store the value in "head"
            #and go to the next node
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            #if the opposite we store the value of list2 in "head" and go to the next node
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        #edge case if the next value of a node is null
        if list1:
            head.next = list1
        if list2:
            head.next = list2
        return dummy.next


#Recursion
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #edge case if the next node is null
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
    #if the head of list1 is less than the head of list 2, add the next value to the merged list
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


    