# Maximal Square

Given an `m x n` binary `matrix` filled with `0`'s and `1`'s, find the largest square containing only `1`'s and *return its area*.

 

## Example 1:
![image](https://user-images.githubusercontent.com/24850908/146651329-9f243bcc-a630-46b0-80eb-8dcbed09e142.png)

#### Input: 
`matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]`

#### Output: 
`4`



## Example 2:
![image](https://user-images.githubusercontent.com/24850908/146651339-297ce8b8-b2c6-4724-b64c-a12e1208b0bf.png)

#### Input: 
`matrix = [["0","1"],["1","0"]]`

#### Output: 
`1`



## Example 3:

#### Input: 
`matrix = [["0"]]`

#### Output: 
`0`
 


## Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 300
- matrix[i][j] is '0' or '1'.
