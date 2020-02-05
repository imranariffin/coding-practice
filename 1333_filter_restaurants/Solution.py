class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        vegan_filtered = [r for r in restaurants if not veganFriendly or r[2]]
        price_filtered = [r for r in vegan_filtered if r[3] <= maxPrice]
        distance_filtered = [r for r in price_filtered if r[4] <= maxDistance]

        def key_fn(r):
            return (-r[1], -r[0])

        sorted_ls = sorted(distance_filtered, key=key_fn)

        return [r[0] for r in sorted_ls]
