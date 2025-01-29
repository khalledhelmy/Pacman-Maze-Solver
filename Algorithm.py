from queue import PriorityQueue

# Get valid neighbors for pathfinding
def get_neighbors(position: tuple[int, int], maze: list[list[int]]) -> list:
    row, col = position
    neighbors = []
    if row > 0 and maze[row - 1][col] == 0:  # Up
        neighbors.append((row - 1, col))
    if row < len(maze) - 1 and maze[row + 1][col] == 0:  # Down
        neighbors.append((row + 1, col))
    if col > 0 and maze[row][col - 1] == 0:  # Left
        neighbors.append((row, col - 1))
    if col < len(maze[0]) - 1 and maze[row][col + 1] == 0:  # Right
        neighbors.append((row, col + 1))
    return neighbors


class Point:
    '''Class to store coordinates and its path'''
    def __init__(self, cordinates: tuple[int, int], path: list[int]):
        self.cordinates = cordinates  
        self.path = path

# A* algorithm
def heuristic(a: tuple[int, int], b: tuple[int, int]) -> int:
    """Heuristic for A* (Manhattan distance)"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze: list[list[int]] , start: tuple[int, int], goal: tuple[int, int]) -> list:
    """
    A* pathfinding algorithm to find the shortest path in a maze.

    Args:
        maze (list[list[int]]): The maze represented as a list of lists of integers,
                                where 0 is a free path and 1 is a wall.
        start (tuple[int, int]): The starting position in the maze as a tuple of (row, col).
        goal (tuple[int, int]): The goal position in the maze as a tuple of (row, col).

    Returns:
        List[Tuple[int, int]]: The shortest path from the start to the goal as a list of 
                               tuples representing positions, or None if no path is found.
    """
  
    queue = PriorityQueue()
    point = Point(start, [start])
    fake = 10000
    cost_count = {start : 0}
    total_cost = cost_count[start] + heuristic(start, goal)
    queue.put((total_cost, cost_count[start], fake, point))

    
    while not queue.empty():
        total_cost, count_so_far, _, point = queue.get()
        if point.cordinates == goal:
            print(len(point.path), point.path)
            return point.path
        
        else:
            for neighbor in get_neighbors(point.cordinates, maze):
                new_path = point.path + [neighbor]
                new_point = Point(neighbor, new_path)
                new_count = count_so_far + 1
                fake += 1
                if neighbor not in cost_count or new_count < cost_count[neighbor]:
                    cost_count[neighbor] = new_count
                    neighbor_total_cost = cost_count[neighbor] + heuristic(neighbor, goal)
                    queue.put((neighbor_total_cost, cost_count[neighbor], fake, new_point))
    return None


# DFS Algorithm
def DFS(maze: list[list[int]] , start: tuple[int, int], goal: tuple[int, int]) -> list:
    """
    Depth-First Search (DFS) algorithm to find a path in a maze.

    Args:
        maze (List[List[int]]): The maze represented as a list of lists of integers,
                                where 0 is a free path and 1 is a wall.
        start (Tuple[int, int]): The starting position in the maze as a tuple of (row, col).
        goal (Tuple[int, int]): The goal position in the maze as a tuple of (row, col).

    Returns:
        List[Tuple[int, int]]: The path from the start to the goal as a list of tuples representing
                               positions, or None if no path is found.
    """
    stack = []
    visited = set()
    point = Point(start,[start])
    stack.append(point)

    while stack:
        visited.add(point.cordinates)
        point = stack.pop()

        if point in visited:
            continue

        if point.cordinates == goal:
            print('DFS',len(point.path), point.path)
            return point.path
        
        else :
            neighbors = []
            for neighbor in get_neighbors(point.cordinates, maze):
                if neighbor not in visited:
                    new_path = point.path + [neighbor]
                    new_point = Point(neighbor,new_path)
                    neighbors.append(new_point)

            neighbors.reverse()
            stack.extend(neighbors)
    return None


