# Insertion Sort List

Given the `head` of a singly linked list, sort the list using **insertion sort**, and return *the sorted list's head*.

The steps of the **insertion sort** algorithm:

1. Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
3. It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.
![image](https://user-images.githubusercontent.com/24850908/146278851-77721b41-6a70-4ebb-9551-4b1a18a6d7f7.png)


 
## Example 1:
![image](https://user-images.githubusercontent.com/24850908/146278888-eaea8300-64b2-4653-a821-e7ae794ffef2.png)

#### Input: 
`head = [4,2,1,3]`

#### Output: 
`[1,2,3,4]`



## Example 2:
![image](https://user-images.githubusercontent.com/24850908/146278927-e2661638-aff0-4811-a778-765406a822a4.png)

#### Input: 
`head = [-1,5,3,4,0]`

#### Output: 
`[-1,0,3,4,5]`
 


## Constraints:
- The number of nodes in the list is in the range [1, 5000].
- -5000 <= Node.val <= 5000
