class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stack = s.split()
        result = len(stack[-1])
        return result