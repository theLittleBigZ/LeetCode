class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for letter in word:
            if letter.isupper():
                count += 1
        if count == 0 or count == len(word):
            return True
        elif count == 1 and word[0].isupper():
            return True
        return False
