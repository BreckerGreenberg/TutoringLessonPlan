# gorlock is the destroyer and she is a booty scratcher
# she has a gyaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat amd she is cuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuute
import pygame
import sys


# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escape the Maze")

# Define the maze as a list of strings
maze = [
    "####################",
    "#                  #",
    "#  ######  ####### #",
    "#  #           #   #",
    "#  #  ####### # #  #",
    "#  #         # #  #",
    "#  #############  #",
    "#                # #",
    "################## #",
    "#                  #",
    "####################",
]

# Player start position
player_pos = [1, 1]

def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "#":
                pygame.draw.rect(screen, BLACK, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            elif cell == " ":
                pygame.draw.rect(screen, WHITE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_player():
    pygame.draw.rect(screen, GREEN, (player_pos[0] * GRID_SIZE, player_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def is_move_valid(new_pos):
    if maze[new_pos[1]][new_pos[0]] != "#":
        return True
    return False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        new_pos = [player_pos[0], player_pos[1] - 1]
        if is_move_valid(new_pos):
            player_pos = new_pos
    if keys[pygame.K_DOWN]:
        new_pos = [player_pos[0], player_pos[1] + 1]
        if is_move_valid(new_pos):
            player_pos = new_pos
    if keys[pygame.K_LEFT]:
        new_pos = [player_pos[0] - 1, player_pos[1]]
        if is_move_valid(new_pos):
            player_pos = new_pos
    if keys[pygame.K_RIGHT]:
        new_pos = [player_pos[0] + 1, player_pos[1]]
        if is_move_valid(new_pos):
            player_pos = new_pos

    # Drawing
    screen.fill(WHITE)
    draw_maze()
    draw_player()

    pygame.display.flip()
    pygame.time.Clock().tick(30)
