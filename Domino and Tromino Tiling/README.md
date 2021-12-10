# Domino and Tromino Tiling

You have two types of tiles: a `2 x 1` domino shape and a tromino shape. You may rotate these shapes.
![image](https://user-images.githubusercontent.com/24850908/145602773-3c9780b7-4289-4f12-ad4e-52a47c138269.png)

Given an integer n, return the number of ways to tile an `2 x n` board. Since the answer may be very large, return it **modulo** `10<sup>9</sup> + 7`.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

## Example 1:
![image](https://user-images.githubusercontent.com/24850908/145602950-18f61871-852e-4aa4-8b4a-782e65388497.png)

#### Input: 
`n = 3`

#### Output: 
`5`

#### Explanation: 
- The five different ways are show above.



## Example 2:

#### Input: 
`n = 1`

#### Output: 
`1`
 


## Constraints:
- 1 <= n <= 1000
