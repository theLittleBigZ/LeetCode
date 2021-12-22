# Reorder List

You are given the head of a singly linked-list. The list can be represented as:

`L0 → L1 → … → Ln - 1 → Ln`

Reorder the list to be on the following form:

`L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

## Example 1:
![image](https://user-images.githubusercontent.com/24850908/147157723-cafab90b-fa12-4722-8fda-0b9af61c3364.png)

#### Input: 
`head = [1,2,3,4]`

#### Output: 
`[1,4,2,3]`

## Example 2:
![image](https://user-images.githubusercontent.com/24850908/147157829-c1e87342-87dc-40df-a5f8-60cbf3c2a5df.png)

#### Input: 
`head = [1,2,3,4,5]`

#### Output: 
`[1,5,2,4,3]`
 


## Constraints:
- The number of nodes in the list is in the range [1, 5 * 10<sup>4</sup>].
- 1 <= Node.val <= 1000
