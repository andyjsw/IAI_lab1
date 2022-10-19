class c_point:
    x = int()
    y = int()
    
    valid = bool()
    visited = False
    start_point = False
    end_point = False
    prev = None
    bonus = 0
    min_distance = 1e9
    is_path = False
    is_teleport = False
    
    def __init__(self, x = 0, y = 0, n_cols = 0, n_rows = 0):
        self.x = x
        self.y = y
        self.adjacent = []

        if x != 0:
            self.adjacent.append([self.x-1, self.y])
            #print(1)
        if x != n_cols-1:
            self.adjacent.append([self.x+1, self.y])
            #print(2)
        if y != 0:
            self.adjacent.append([self.x, self.y-1])
            #print(3)
        if y != n_rows - 1:
            self.adjacent.append([self.x, self.y+1])
            #print(4)
        #print(len(self.adjacent))
        
    def __eq__(self, o):
         return self.x == o.x and self.y == o.y


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m' 
    YELBG = '\x1b[0;30;43m'
    REDBG = '\x1b[0;30;41m'
    GREENBG = '\x1b[0;30;42m'
        

def readMaze(fileName):
    file = open(fileName, 'r')
    lines = file.readlines()
    file.close()

    n_bonus = int(lines[0])
    
    n_rows = len(lines[n_bonus + 1 :]) if lines[-1][0] == 'x' else len(lines[n_bonus + 1 : -1])
    n_cols = len(lines[n_bonus + 1]) - 1
    
    #a[i][j] i:dòng j:cột
    
    maze = list()
    for y in range (n_rows):
        maze.append([])
        for x in range(n_cols):
            maze[y].append(c_point(x, y, n_cols, n_rows))
            
    start_point = c_point()       
    end_point = c_point()
    for y in range(n_rows):
        line = str()
        for x in range(n_cols):
            line += lines[n_bonus + y + 1][x]

            if x == 0 or x == n_cols - 1:
                if lines[n_bonus + y + 1][x] == ' ':
                    maze[y][x].end_point = True
                    end_point = c_point(x, y)
            if y == 0 or y == n_rows - 1:
                if lines[n_bonus + y + 1][x] == ' ':
                    maze[y][x].end_point = True
                    end_point = c_point(x, y)
            
            maze[y][x].valid = False if lines[n_bonus + y + 1][x] == 'x' else True

            if lines[n_bonus + y + 1][x] == 'S':
                maze[y][x].start_point = True
                maze[y][x].min_distance = 0
                start_point = c_point(x, y)

    for line in lines[1 : n_bonus + 1]:
        bonus = list(map(int, line.split(' ')))
        maze[bonus[0]][bonus[1]].bonus = bonus[2]
        
    if lines[-1][0] != 'x':
        temp = list(map(int, lines[-1].split(' ')))
        maze[temp[0]][temp[1]].is_teleport = True
        maze[temp[2]][temp[3]].is_teleport = True
        maze[temp[0]][temp[1]].adjacent.append([temp[3],temp[2]])
        maze[temp[2]][temp[3]].adjacent.append([temp[1],temp[0]])
            
    return maze, n_rows, n_cols, start_point, end_point

def printMaze(maze, n_rows, n_cols):
    for y in range(n_rows):
        line = str()
        for x in range(n_cols):
            if maze[y][x].valid == False:
                line += f'{color.YELBG}x{color.END}'
            elif maze[y][x].start_point == True:
                line += f'{color.RED}{color.BOLD}S{color.END}'
            else:
                if maze[y][x].bonus != 0:
                    if maze[y][x].visited == False:
                        line += f'{color.GREEN}{color.BOLD}+{color.END}'
                    if maze[y][x].visited == True:
                        if maze[y][x].is_path == False:
                            line += f'{color.REDBG}{color.BOLD}+{color.END}'
                        else:
                            line += f'{color.GREENBG}{color.BOLD}+{color.END}'
                else: 
                    if maze[y][x].visited == False:
                        if maze[y][x].is_teleport == False:
                            line += ' '
                        else:
                            line += 'i'
                    
                    else:
                        if maze[y][x].is_path == True:
                            if maze[y][x].is_teleport == False:
                                line += f'{color.GREENBG} {color.END}'
                            else:
                                line += f'{color.GREENBG}i{color.END}'
                        else:
                            if maze[y][x].is_teleport == False:
                                line += f'{color.REDBG} {color.END}'
                            else:
                                line += f'{color.REDBG}i{color.END}'
        print(line)