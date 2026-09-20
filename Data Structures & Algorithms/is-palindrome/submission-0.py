class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        left = 0
        right = len(s) - 1
        while right > left:
            if s[left] == s[right]:
                right -= 1
                left += 1
            else:
                return False
        return True