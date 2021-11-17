# Kth Smallest Number in Multiplication Table
Nearly everyone has used the Multiplication Table. The multiplication table of size `m x n` is an integer matrix `mat` where `mat[i][j] == i * j` (**1-indexed**).

Given three integers `m`, `n`, and `k`, return the kth smallest element in the `m x n` *multiplication table*.

 

## Example 1:
![3 by 3 multiplication table](https://user-images.githubusercontent.com/24850908/142127711-424e006e-6a0b-4c71-9c7e-e2f45c553a7c.png)
#### Input: 
`m = 3, n = 3, k = 5`

#### Output: 
`3`

#### Explanation: 
`The 5th smallest number is 3.`



## Example 2:
![2 by 3 multiplication table](https://assets.leetcode.com/uploads/2021/05/02/multtable2-grid.jpg)
#### Input: 
`m = 2, n = 3, k = 6 `

#### Output: 
`6`

#### Explanation: 
`The 6th smallest number is 6.`
 


## Constraints:
- 1 <= m, n <= 3 * 10^4
- 1 <= k <= m * n
