# Linked List Cycle II

Given the `head` of a linked list, return *the node where the cycle begins. If there is no cycle, return* `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (**0-indexed**). It is `-1` if there is no cycle. **Note that** `pos` **is not passed as a parameter**.

**Do not modify** the linked list.

 

## Example 1:
![image](https://user-images.githubusercontent.com/24850908/150195281-c942ac36-e1d5-4b6c-8e74-72e005527454.png)

#### Input: 

`head = [3,2,0,-4], pos = 1`

#### Output: 

`tail connects to node index 1`

#### Explanation: 

`There is a cycle in the linked list, where tail connects to the second node.`



## Example 2:
![image](https://user-images.githubusercontent.com/24850908/150195375-350c95ba-5cc5-482d-8070-e301714efd4b.png)

#### Input: 

`head = [1,2], pos = 0`

#### Output: 

`tail connects to node index 0`

#### Explanation: 

`There is a cycle in the linked list, where tail connects to the first node.`



## Example 3:
![image](https://user-images.githubusercontent.com/24850908/150195464-6f7ffd0f-2880-4f8c-ba94-1b19f49ca51f.png)

#### Input: 

`head = [1], pos = -1`

#### Output: 

`no cycle`

#### Explanation: 

`There is no cycle in the linked list.`

 

## Constraints:
- The number of the nodes in the list is in the range `[0, 104]`.
- -10<sup>5</sup> <= `Node.val` <= 10<sup>5</sup>
- `pos` is `-1` or a valid index in the linked-list.
