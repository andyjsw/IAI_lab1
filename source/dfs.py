from source import display as ds
from source import read_maze
import time
import threading

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
GREY = (192,192,192)
GREY_YELLOW = (178, 156, 76)
VIOLET = (138,43,226)

def _exit():
    while True:
        for event in ds.pygame.event.get():
            if event.type == ds.pygame.QUIT:
                ds.pygame.quit()
                ds.sys.exit(0)
                return
    return

def main(maze, n_rows, n_cols, start, end):
    ds.N_COLS = n_cols
    ds.N_ROWS = n_rows
    ds.main("DFS")

    draw(maze, n_rows, n_cols)
        
    ds.pygame.display.update()

    
    x = threading.Thread(target=_exit)
    x.start()
    dfs(maze, n_rows, n_cols, start, end)

    
def draw(maze, n_rows, n_cols):
    blockSize = 20 #Set the size of the grid block
    sysfont = ds.pygame.font.get_default_font()
    font = ds.pygame.font.SysFont(None, 35)
    for y in range(n_rows):
        for x in range(n_cols):
            color = BLACK
            if maze[y][x].valid == False:
                color = BLACK
            elif maze[y][x].start_point == True:
                color = RED
            else:
                if maze[y][x].bonus != 0:
                    if maze[y][x].visited == False:
                        color = GREEN
                    if maze[y][x].visited == True:
                        if maze[y][x].is_path == False:
                            color = YELLOW
                        else:
                            color = BLUE
                else: 
                    if maze[y][x].visited == False:
                        if maze[y][x].is_teleport == False:
                            color = WHITE
                        else:
                            color = VIOLET
                    
                    else:
                        if maze[y][x].is_path == True:
                            if maze[y][x].is_teleport == False:
                                color = BLUE
                            else:
                                color = VIOLET
                        else:
                            if maze[y][x].is_teleport == False:
                                color = YELLOW
                            else:
                                color = YELLOW
            
            rect = ds.pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            ds.SCREEN.fill(color, rect) 


def dfs(maze, n_rows, n_cols, start, end):
    maze[start.y][start.x].prev = (start.x, start.y)
    maze[start.y][start.x].visited = True
    blockSize = 20 
    st = []
    st.append((maze[start.y][start.x].x, maze[start.y][start.x].y))
    x = int
    y = int
    while len(st) != 0:
        cur_pos = st.pop()
        x = cur_pos[0]
        y = cur_pos[1]
        if maze[y][x].valid == False:
            continue
    
        if (maze[y][x] != start):
            rect = ds.pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            ds.SCREEN.fill(YELLOW, rect) 
            ds.pygame.display.update()
        time.sleep(0.1)

        if (maze[y][x] == end):
            break

        for next in maze[y][x].adjacent:
            if maze[next[1]][next[0]].visited == False:
                st.append((next[0], next[1]))
                maze[next[1]][next[0]].visited = True
                maze[next[1]][next[0]].prev = (x, y)
                #if maze[y][x].is_teleport:
                #    print(x, y, maze[y][x].prev)

    while (x != maze[y][x].prev[0] or y != maze[y][x].prev[1]):
        rect = ds.pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
        ds.SCREEN.fill(BLUE, rect) 
        ds.pygame.display.update()
        time.sleep(0.1)
        # print(x, y, end=" ")
        x, y = maze[y][x].prev




if __name__ == "__main__":
    main()
