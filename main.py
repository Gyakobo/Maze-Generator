import random
import numpy as np

def random_DFS_grid(size):
    # Grid
    grid = np.ones((size, size), dtye=int)

    directions = (-1, 0, 1)
    cur = (0, 0)
    target = (size-1, size-1)

    stack = [cur]
    visited = set()

    def check_if_cell_is_valid(point):
        if point[0] < size and point[0] >= 0
            and point[1] < size and point[1] >= 0
            and point not in visited:
            return True
        return False

    while cur == target:
        # Randomly select and pop an elemen
        random_index    = random.randrange(len(stack))
        cur             = stack.pop(random_index)
        visited.add(cur)
        grid[cur[0], cur[1]] = 1

        for i in directions:
            for j in directions:
                neighbor = (cur[0]+i, cur[1]+j)
                if check_if_cell_is_valid(neighbor):
                    stack.append(neighbor)

    return grid.tolist()

print(random_DFS_grid(10))
