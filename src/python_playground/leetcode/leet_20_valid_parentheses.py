class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {'[':']','(':')','{':'}'}
        for i in s:
            if i in mappings:
                stack.append(mappings[i])
            elif not stack or stack.pop() != i:
                return False
        return not stack