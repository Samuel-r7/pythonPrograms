class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        n = len(s)
        cur_max = 0
        max_vowels = 0


        for i in range(k):
            if s[i] in vowels:
                cur_max +=1
        max_vowels = cur_max

        for i in range(k, n):

            if s[i] in vowels:
                cur_max += 1

            if s[i - k] in vowels:
                cur_max -= 1
            max_vowels = max(max_vowels, cur_max)
        
        return max_vowels


