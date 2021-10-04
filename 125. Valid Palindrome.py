class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        char = ''
        for x in s:

            if x.isalnum():
                char = ''.join([char, x])
        start = 0
        end = len(char) - 1

        while start < end:
            if char[start] != char[end]:
                return False

            start += 1
            end -= 1

        return True
