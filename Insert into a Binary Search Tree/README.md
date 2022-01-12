# Insert into a Binary Search Tree

You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return *the root node of the BST after the insertion*. It is **guaranteed** that the new value does not exist in the original BST.

**Notice** that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return **any of them**.

 

## Example 1:
![image](https://user-images.githubusercontent.com/24850908/149214103-55bd28cd-f366-41c6-a2ed-baaca9f50d3f.png)

#### Input: 

`root = [4,2,7,1,3], val = 5`

#### Output: 

`[4,2,7,1,3,5]`

#### Explanation: 

`Another accepted tree is:`
![image](https://user-images.githubusercontent.com/24850908/149214251-f8e54b96-2d03-4cfe-822c-ef239b6475dd.png)



## Example 2:

#### Input: 

`root = [40,20,60,10,30,50,70], val = 25`

#### Output: 

`[40,20,60,10,30,50,70,null,null,25]`



## Example 3:

#### Input: 

`root = [4,2,7,1,3,null,null,null,null,null,null], val = 5`

#### Output: 

`[4,2,7,1,3,5]`
 


## Constraints:
- The number of nodes in the tree will be in the range [0, 10<sup>4</sup>].
- -10<sup>8</sup> <= `Node.val` <= 10<sup>8</sup>
- All the values `Node.val` are **unique**.
- -10<sup>8</sup> <= `val` <= 10<sup>8</sup>
- It's **guaranteed** that `val` does not exist in the original BST.
