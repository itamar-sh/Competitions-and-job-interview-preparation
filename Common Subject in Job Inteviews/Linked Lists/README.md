## Remove Duplicates From an Unsorted Linked List - 1836 - Easy
### Problem
Write a removeDuplicates() function that takes a list and deletes any duplicate nodes from the list. The list is not sorted. 
For example if the linked list is 12->11->12->21->41->43->21 then removeDuplicates() should convert the list to 12->11->21->41->43
### requirement:
We can solve in O(n*log(n)) in time with O(1) space
We can solve in O(n) in time with O(n) space
### Trick:
marge sort for O(n*log(n)) time - change order of elements!
set for O(n) time + O(n) space

## Partition List - 86 - Medium
### Problem
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
### Example 1
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
### Example 2
Input: head = [2,1], x = 2
Output: [1,2]
### requirement:
O(1) space, O(n) time
### Trick
use two dummies nodes
one for nodes smaller than n and one for bigger
