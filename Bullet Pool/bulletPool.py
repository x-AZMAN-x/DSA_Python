from collections import deque

class BulletPool:
    def __init__(self, pool_size):
        # Pre-create all bullet objects at game start
        self.pool = deque(
            [{'id': i, 'active': False} for i in range(pool_size)]
        )

        print(f"Bullet pool created with {pool_size} bullets.")

    def fire(self, x, y, direction):
        if not self.pool:
            print("No bullets available! Reload first.")
            return None

        # Get bullet from pool
        bullet = self.pool.popleft()

        bullet['active'] = True
        bullet['x'] = x
        bullet['y'] = y
        bullet['dir'] = direction

        print(
            f"FIRED bullet #{bullet['id']} "
            f"at ({x}, {y}) going {direction}"
        )

        return bullet

    def recycle(self, bullet):
        # When bullet hits something, return it to the pool
        bullet['active'] = False
        self.pool.append(bullet)

        print(f"Bullet #{bullet['id']} recycled back to pool.")


# Example Usage
pool = BulletPool(3)

b1 = pool.fire(10, 20, "RIGHT")
b2 = pool.fire(15, 25, "UP")

# b1 hits enemy and returns
pool.recycle(b1)

# Reuses b1's slot
b3 = pool.fire(5, 5, "LEFT")