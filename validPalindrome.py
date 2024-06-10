class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(letter.lower() for letter in s if letter.isalnum())

        return word == word[::-1]