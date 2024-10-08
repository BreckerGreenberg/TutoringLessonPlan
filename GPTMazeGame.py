import os

# Define the maze as a list of strings
maze = [
    "####################",
    "#                  #",
    "#  #",
    "#     #",
    "#    #",
    "#  #",
    "#    #",
    "#                 #",
    "# #",
    "#                  #",
    "####################",
]

# Player start position
player_pos = [1, 1]

def draw_maze():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if [x, y] == player_pos:
                print('P', end='')  # Player representation
            else:
                print(cell, end='')
        print()  # New line after each row

def is_move_valid(new_pos):
    if maze[new_pos[1]][new_pos[0]] != "#":
        return True
    return False

# Main game loop
while True:
    draw_maze()
    move = input("Move (WASD to move, Q to quit): ").lower()

    if move == 'q':
        break
    elif move == 'w':
        new_pos = [player_pos[0], player_pos[1] - 1]
        if is_move_valid(new_pos):
            player_pos = new_pos
    elif move == 's':
        new_pos = [player_pos[0], player_pos[1] + 1]
        if is_move_valid(new_pos):
            player_pos = new_pos
    elif move == 'a':
        new_pos = [player_pos[0] - 1, player_pos[1]]
        if is_move_valid(new_pos):
            player_pos = new_pos
    elif move == 'd':
        new_pos = [player_pos[0] + 1, player_pos[1]]
        if is_move_valid(new_pos):
            player_pos = new_pos
    else:
        print("Invalid move! Use W (up), A (left), S (down), D (right), or Q to quit.")

print("Thanks for playing!")
