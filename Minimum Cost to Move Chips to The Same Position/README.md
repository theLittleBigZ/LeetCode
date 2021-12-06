# Minimum Cost to Move Chips to The Same Position

We have `n` chips, where the position of the `i<sup>th</sup>` chip is `position[i]`.

We need to move all the chips to **the same position.** In one step, we can change the position of the `i<sup>th</sup>` chip from `position[i]` to:
- `position[i] + 2` or `position[i] - 2` with `cost = 0`.
- `position[i] + 1` or `position[i] - 1` with `cost = 1`.

Return *the minimum cost* needed to move all the chips to the same position.

 

## Example 1:
![image](https://user-images.githubusercontent.com/24850908/144881821-1ba61eb2-b029-4672-b785-482ffd3c6e3f.png)

#### Input: 
`position = [1,2,3]`

#### Output: 
`1`

#### Explanation: 
- First step: Move the chip at position 3 to position 1 with cost = 0.
- Second step: Move the chip at position 2 to position 1 with cost = 1.
- Total cost is 1.



## Example 2:
![image](https://user-images.githubusercontent.com/24850908/144881918-a55f49a7-31f1-4bb7-9647-2174db117d79.png)

#### Input: 
`position = [2,2,2,3,3]`

#### Output: 
`2`

#### Explanation: 
- `We can move the two chips at position  3 to position 2. Each move has cost = 1.` 
- `The total cost = 2.`



## Example 3:

#### Input: 
`position = [1,1000000000]`

#### Output: 
`1`
 


## Constraints:
- 1 <= position.length <= 100
- 1 <= position[i] <= 10<sup>9</sup>
