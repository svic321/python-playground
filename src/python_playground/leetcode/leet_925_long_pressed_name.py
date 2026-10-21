class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        count = 0
        for i, j in enumerate(typed):
            if count < len(name) and name[count] == j:
                count += 1
            elif i == 0 or typed[i-1] != j:
                return False
        return count == len(name)
