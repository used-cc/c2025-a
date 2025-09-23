import os
import msvcrt

MAZE = [
    "##########",
    "#@     # #",
    "# ### #  #",
    "#   # ####",
    "### #    #",
    "#   ###  #",
    "# #   #  #",
    "# ### ####",
    "#      △#",
    "##########"
]

PLAYER = '@'
EXIT = '△'
WALL = '#'
SPACE = ' '

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_pos(maze, char):
    for y, row in enumerate(maze):
        x = row.find(char)
        if x != -1:
            return y, x
    return None

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def main():
    maze = [list(row) for row in MAZE]
    player_y, player_x = find_pos(MAZE, PLAYER)

    while True:
        clear_screen()
        print_maze(maze)
        print("请用WASD控制移动")
        key = msvcrt.getch().decode('utf-8').lower()
        dy, dx = 0, 0
        if key == 'w':
            dy = -1
        elif key == 's':
            dy = 1
        elif key == 'a':
            dx = -1
        elif key == 'd':
            dx = 1
        else:
            continue

        new_y, new_x = player_y + dy, player_x + dx
        if maze[new_y][new_x] == WALL:
            continue
        if maze[new_y][new_x] == EXIT:
            clear_screen()
            maze[player_y][player_x] = SPACE
            maze[new_y][new_x] = PLAYER
            print_maze(maze)
            print("恭喜通关")
            break

        maze[player_y][player_x] = SPACE
        maze[new_y][new_x] = PLAYER
        player_y, player_x = new_y, new_x

if __name__ == "__main__":
    main()