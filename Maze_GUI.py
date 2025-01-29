import pygame
import random

# Constants
WIDTH, HEIGHT = 900, 600
CELL_SIZE = 24  
FPS = 60

# Colors (RGB)
WHITE = '#ffffff'
LIGHT_BLUE = '#0488FF'

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHT_GREEN = '#59CE8F'
LIGHT_RED = '#F72C5B'

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Complex Maze")
clock = pygame.time.Clock()




def generate_maze(rows, cols):
    # Initialize the maze with walls (1)
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    stack = []

    # Start from the top-left corner
    start_x, start_y = 0, 0
    end_x, end_y = cols - 1, rows - 1

    stack.append((start_x, start_y))
    visited[start_y][start_x] = True
    maze[start_y][start_x] = 0

    # Define movement directions (skipping by 2 to preserve walls)
    directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]

    # Iterative DFS to carve the maze
    while stack:
        current_x, current_y = stack[-1]
        unvisited_neighbors = []

       
        for dx, dy in directions:
            nx, ny = current_x + dx, current_y + dy
            if 0 <= nx < cols and 0 <= ny < rows and not visited[ny][nx]:
                unvisited_neighbors.append((nx, ny))

        if unvisited_neighbors:
            # Randomly pick a neighbor
            next_x, next_y = random.choice(unvisited_neighbors)
            stack.append((next_x, next_y))
            visited[next_y][next_x] = True
            maze[next_y][next_x] = 0

            # Remove the wall between the current and next cell
            wall_x, wall_y = (current_x + next_x) // 2, (current_y + next_y) // 2
            if 0 <= wall_x < cols and 0 <= wall_y < rows:
                maze[wall_y][wall_x] = 0
        else:
            # Backtrack if no unvisited neighbors
            stack.pop()

    # Ensure the goal (bottom-right corner) is reachable
    maze[end_y][end_x] = 0

    for _ in range(rows * cols // 5):  
        x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
        if 0 <= x < cols and 0 <= y < rows:
            maze[y][x] = 0

    return maze



# Draw the maze on the screen
def draw_maze(maze, path_crossed_A=None,path_crossed_DFS=None):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            color = LIGHT_GREEN if path_crossed_A and (row, col) in path_crossed_A else(LIGHT_RED if path_crossed_DFS and (row, col) in path_crossed_DFS else (LIGHT_BLUE if maze[row][col] == 1 else WHITE))
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Draw agent at a given position
def draw_agent(position, color=YELLOW):
    row, col = position
    pygame.draw.circle(
        screen,
        color,
        (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
        CELL_SIZE // 3
    )


# Get random position for goal
def get_random_goal_position(maze):
    rows, cols = len(maze), len(maze[0])
    while True:
        row, col = random.randint(12, rows - 6), random.randint(0, cols - 1)
        if maze[row][col] == 0 and (maze[row-1][col] == 0 or maze[row][col-1] == 0 or maze[row+1][col] == 0 or maze[row][col+1] == 0):  # Ensure the goal is placed in an open path
            return (row, col)
        
# Draw the goal 
def draw_goal(position, color=RED):
    row, col = position
    pygame.draw.circle(
        screen,
        color,
        (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
        CELL_SIZE // 5
    )
