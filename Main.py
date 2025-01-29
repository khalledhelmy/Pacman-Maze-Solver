from Maze_GUI import *
from Algorithm import a_star, DFS

ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Generate maze and set up positions
maze = generate_maze(ROWS, COLS)
pacman_position = (0, 0)
pellet_position = get_random_goal_position(maze)


font = pygame.font.Font(None, 36)  
running = True
path_A = None
path_DFS = None
path_crossed_A = set()  # To track the squares Pac-Man crosses
path_crossed_DFS = set()  # To track the squares Pac-Man crosses
path_length_A = None  # To store the length of the A star path
path_length_DFS = None  # To store the length of the DFS path

while running:
    screen.fill(LIGHT_BLUE)
    draw_maze(maze,path_crossed_A,path_crossed_DFS)  
    draw_agent(pacman_position)  
    draw_goal(pellet_position)  

    # Display the path length if it is available
    if path_length_A is not None and path_length_DFS is not None:
        
        text_A = f"Path Length A*: {path_length_A}"
        text_DFS = f"Path Length DFS: {path_length_DFS}"

        length_text_A = font.render(text_A, True, LIGHT_GREEN)
        length_text_DFS = font.render(text_DFS, True, LIGHT_RED)

        max_width = max(length_text_A.get_width(), length_text_DFS.get_width())
        max_height = max(length_text_A.get_height(), length_text_DFS.get_height())

        bg_rect_A = pygame.Rect(WIDTH - max_width - 15,0, max_width + 15, max_height + 10)
        bg_rect_DFS = pygame.Rect(WIDTH - max_width - 15, 30, max_width + 15, max_height + 10)

        # Draw the background rectangle for A*
        pygame.draw.rect(screen, "#ffffff", bg_rect_A)
        screen.blit(length_text_A, (bg_rect_A.x + 5, bg_rect_A.y + 5))

        # Draw the background rectangle for DFS
        pygame.draw.rect(screen, "#ffffff", bg_rect_DFS)
        screen.blit(length_text_DFS, (bg_rect_DFS.x, bg_rect_DFS.y + 5))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Regenerate the maze
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Reset maze
                maze = generate_maze(HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE)
                pacman_position = (0, 0)
                pellet_position = get_random_goal_position(maze)  # Randomize pellet
                path_A = None
                path_DFS = None
                path_crossed_A.clear()
                path_crossed_DFS.clear()
                path_length_A = None
                path_length_DFS = None
            
            # Solve maze using A* algorithm
            if event.key == pygame.K_a:
                pacman_position = (0, 0)
                path_A = a_star(maze, pacman_position, pellet_position)  
                if path_A:
                    path_length_A = len(path_A) 
                    # Animate Pac-Man's movement along the path (if a path exists)
                    for step in path_A:  
                        pacman_position = step  
                        path_crossed_A.add(step)  
                        
                        draw_maze(maze,path_crossed_A,path_crossed_DFS)  
                        draw_agent(pacman_position)  
                        draw_goal(pellet_position)  
                        pygame.display.update()  
                        pygame.time.delay(100)  
                

            if event.key == pygame.K_d:
                pacman_position = (0, 0)
                path_DFS = DFS(maze, pacman_position, pellet_position)  # Call A* algorithm
                if path_DFS:
                    path_length_DFS = len(path_DFS)  
                    # Animate Pac-Man's movement along the path (if a path exists)
                    for step in path_DFS:  
                        pacman_position = step 
                        path_crossed_DFS.add(step) 
                        draw_maze(maze, path_crossed_A ,path_crossed_DFS)  
                        draw_agent(pacman_position)  
                        draw_goal(pellet_position)  
                        pygame.display.update()  
                        pygame.time.delay(100)  
    
    

    

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()