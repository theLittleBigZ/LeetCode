#warmr0bot
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remains = [0] * 60
        total = 0
        for t in time:
            need = t % 60
            total += remains[-need % 60]  # equivalent to (60 - need) % 60
            remains[need] += 1
        return total
