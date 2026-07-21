class Solution:
    def isValid(self, s: str) -> bool:
        hs={
            ')':'(',
            '}':'{',
            ']':'[',
        }
        stack=[]
        for ch in s:
            if ch not in hs:
                stack.append(ch)
            else:
                if not stack:
                    return False
                else:
                    popped= stack.pop()
                    if popped != hs[ch]:
                        return False
        return not stack 