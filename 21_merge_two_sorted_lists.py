# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
[
 {val: 1, next: 2},
 {val: 1, next: 2},
 
node1.next = node1
]

let dummy = ListNode(0)
var node = dummy

var l1 = l1
var l2 = l2

while l1 != nil && l2 != nil {
    if l1!.val < l2!.val {
        node.next = l1
        l1 = l1!.next
    } else {
        node.next = l2
        l2 = l2!.next
    }
    node = node.next!
}

node.next = l1 ?? l2

return dummy.next
'''

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if list1 == None and list2 == None:
        #     return []
        # if list1 == None:
        #     return list2
        # elif list2 == None:
        #     return list1
            
        dummy = ListNode()
        node = dummy
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return dummy.next
        
        
'''
make a gh repo link of two questions
Input: list1 = [1,2,4], list2 = [1,3,4]
Expected Output: [1,1,2,3,4,4]
    list1 = [1, 2, 4]
             ^
    list2 = [1, 3, 4]
             ^
             
    dummy = {val: 0, next: None}
    node = {val: 4, next: list1}
    list1 = {val: 4, next: None}
    list2 = None
    
    
    To traverse linked-list: 
    list1.val
    list1.next 
    
Pseudocode: 
    Set up a node to be the traversal pointer of the new linked-list.
    traverse each linked-list until you reach the tail of each linked-list
        compare the values of each current list node and set the new node's next to be the smaller value and shift the node of that chosen list to its next node
        shift the new list's node to its next to set it up for the next insertion
    Finally, set the new list's last node to be the remaining node of the two original lists.
    Return the head of the merged linked list
'''
