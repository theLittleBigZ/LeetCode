# Linked List Random Node

Given a singly linked list, return a random node's value from the linked list. Each node must have the **same probability** of being chosen.

Implement the `Solution` class:
- `Solution(ListNode head)` Initializes the object with the integer array nums.
- `int getRandom()` Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be choosen.
 


## Example 1:
![image](https://user-images.githubusercontent.com/24850908/148601521-59fde97b-4b84-461e-ac90-8e90ea4c19ae.png)

#### Input

`["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]`

`[[[1, 2, 3]], [], [], [], [], []]`

#### Output

`[null, 1, 3, 2, 2, 3]`

#### Explanation
- `Solution solution = new Solution([1, 2, 3]);`
- `solution.getRandom(); // return 1`
- `solution.getRandom(); // return 3`
- `solution.getRandom(); // return 2`
- `solution.getRandom(); // return 2`
- `solution.getRandom(); // return 3`
- `// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.`
 


## Constraints:
- The number of nodes in the linked list will be in the range [1, 10<sup>4</sup>].
- -10<sup>4</sup> <= `Node.val` <= 10<sup>4</sup>
- At most 10<sup>4</sup> calls will be made to `getRandom`.
