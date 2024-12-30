import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import numpy as np

from main import *

def generate_maze(width, height):
    # Initialize grid
    grid = np.zeros((height, width), dtype=int)  # 0 for walls, 1 for passages
    visited = np.zeros_like(grid, dtype=bool)

    # Directions: (dx, dy)
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    
    # Starting position
    start_x, start_y = random.randrange(1, width, 2), random.randrange(1, height, 2)
    stack = [(start_x, start_y)]
    grid[start_y, start_x] = 1
    visited[start_y, start_x] = True

    # Target position
    target_x, target_y = width - 1, height - 1

    frames = []  # For animation frames

    current_x, current_y = 0, 0
    while stack:
        current_x, current_y = stack[-1]
        unvisited_neighbors = []

        for dx, dy in directions:
            nx, ny = current_x + dx, current_y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and not visited[ny, nx]:
                unvisited_neighbors.append((nx, ny))

        if unvisited_neighbors:
            nx, ny = random.choice(unvisited_neighbors)
            grid[(current_y + ny) // 2, (current_x + nx) // 2] = 1  # Remove wall
            grid[ny, nx] = 1  # Mark passage
            visited[ny, nx] = True
            stack.append((nx, ny))
        else:
            stack.pop()

        # Save grid state for animation
        frames.append(grid.copy())

    return grid, frames

def animate_maze(frames, interval=50):
    fig, ax = plt.subplots()
    ax.axis('off')
    img = ax.imshow(frames[0], cmap='binary', interpolation='nearest')

    def update(frame):
        img.set_data(frame)
        return img,

    ani = animation.FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)

    # Uncomment to save a .GIF file 
    # ani.save("./miscellaneous/maze.gif", writer="pillow", fps=1000 // interval) 
    # print(f"Animation saved")

    plt.show()


# Maze dimensions (must be odd)
width, height = 21, 21 
maze, animation_frames = generate_maze(width, height)
animate_maze(animation_frames)
