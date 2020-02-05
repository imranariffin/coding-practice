class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        ordered = sorted(
            [(i, height) for (i, height) in enumerate(arr)],
            key=lambda x: x[1],
        )
        mem = [1 for _ in arr]

        for (i, height) in ordered:
            maxcount = 0

            j = i - 1
            while j >= 0 and arr[j] < arr[i] and i - j <= d:
                maxcount = max(maxcount, mem[j])
                j -= 1

            j = i + 1
            while j < len(arr) and arr[j] < arr[i] and j - i <= d:
                maxcount = max(maxcount, mem[j])
                j += 1
            mem[i] = maxcount + 1

        return max(mem)

