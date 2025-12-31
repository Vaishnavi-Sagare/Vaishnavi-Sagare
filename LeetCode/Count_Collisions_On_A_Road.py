class Solution:
    def countCollisions(self, directions: str) -> int:

        n = len(directions)
        i = 0
        j = n - 1

        # Skip all L's at the beginning (they move left → no collision)
        while i < n and directions[i] == 'L':
            i += 1

        # Skip all R's at the end (they move right → no collision)
        while j >= 0 and directions[j] == 'R':
            j -= 1

        collision = 0

        # Inside this range, every R or L collides
        for k in range(i, j + 1):
            if directions[k] != 'S':
                collision += 1

        return collision
