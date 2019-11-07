class Solution:
    def divisorGame(self, n: int) -> bool:
        return self.helper(n, True)

    def helper(self, n: int, isalice: bool) -> bool:
        if isalice and n == 1:
            return False
        if not isalice and n == 1:
            return True

        result = set()
        for i in range(1, n):
            if n%i == 0:
               result.add(self.helper(n-i, not isalice))

        return (
            any(result) if isalice
            else all(result)
        )

