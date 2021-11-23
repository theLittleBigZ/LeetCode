# Largest Component Size by Common Factor

You are given an integer array of unique positive integers `nums`. Consider the following graph:
- There are `nums.length` nodes, labeled `nums[0]` to `nums[nums.length - 1]`,
- There is an undirected edge between `nums[i]` and `nums[j]` if `nums[i]` and `nums[j]` share a common factor greater than `1`.

Return the size of the largest connected component in the graph.

 

## Example 1:
![image](https://user-images.githubusercontent.com/24850908/143071167-4d7b2dcb-c112-4a8a-a289-adca013894a3.png)
#### Input: 
`nums = [4,6,15,35]`

#### Output: 
`4`



## Example 2:
![image](https://user-images.githubusercontent.com/24850908/143071705-a9ea3ad3-0e80-4552-a7ac-e031f167d8da.png)
#### Input: 
`nums = [20,50,9,63]`

#### Output: 
`2`



## Example 3:
![image](https://user-images.githubusercontent.com/24850908/143071725-dc4ab2ed-f1d0-4d9f-93c0-3c9310e32471.png)
#### Input: 
`nums = [2,3,6,7,4,12,21,39]`

#### Output: 
`8`
 


## Constraints:
- 1 <= nums.length <= 2 * 10<sup>4</sup>
- 1 <= nums[i] <= 10<sup>5</sup>
- All the values of `nums` are **unique**.
