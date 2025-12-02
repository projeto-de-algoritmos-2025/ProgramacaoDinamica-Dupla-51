from typing import List
from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # adiciona bordas 1 nas extremidades
        arr = [1] + [x for x in nums if x > 0] + [1]
        n = len(arr)

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            # max moedas estourando balões estritamente entre (left, right)
            if left + 1 >= right:
                return 0
            best = 0
            for k in range(left + 1, right):
                coins = arr[left] * arr[k] * arr[right]
                coins += dp(left, k) + dp(k, right)
                if coins > best:
                    best = coins
            return best

        return dp(0, n - 1)
