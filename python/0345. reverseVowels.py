# 2 pointers
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set('aeiouAEIOU')
        i, j = 0, len(s)-1
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            else:
                if s[i] not in vowels:
                    i += 1
                if s[j] not in vowels:
                    j -= 1
        return ''.join(s)

# 2 queues
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set('aeiou')
        indices, letters = deque(), deque()
        for i, ch in enumerate(s):
            if ch.lower() in vowels:
                indices.append(i)
                letters.appendleft(ch)
        for i, ch in zip(indices, letters):
            s[i] = ch
        return ''.join(s)
