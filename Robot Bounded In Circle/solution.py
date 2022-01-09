class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = {"L": 0 + 1j, "R": 0 - 1j}
        pos = 0j
        face = 1j
        for _ in range(4):
            for c in instructions:
                if c in "LR":
                    face *= dirs[c]
                else:
                    pos += face
        return pos == 0j
