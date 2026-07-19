class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len=min_len = min(len(s) for s in strs)
        i=0
        while i<min_len:
            for s in strs:
                if s[i]!=strs[0][i]:
                    return s[:i]
            i+=1
        return strs[0][:i]