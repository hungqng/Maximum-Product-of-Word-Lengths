# 318. Maximum Product of Word Lengths

# Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lookup = defaultdict(set)
        for w in words:
            lookup[w] = set(w)
        def dont_share(s, t):
            if lookup[s] & lookup[t]:
                return False
            return True
        
        mx = 0
        for i in words:
            for j in words:
                if dont_share(i, j):
                    mx = max(mx, len(i) * len(j))
        return mx