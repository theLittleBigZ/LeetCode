class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ret = 0
        for op in operations:
            if "++" in op:
                ret += 1
            elif "--" in op:
                ret -= 1
        return ret
