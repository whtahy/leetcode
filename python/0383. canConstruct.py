class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        return len(ransomNote - magazine) == 0
