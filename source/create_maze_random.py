from random import randint, choice

class point:
    x = int()
    y = int()

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y


def run(filename, rowmin = 10, rowmax = 15, colmin = 20, colmax = 30, bonus = 0, teleport = False):
    n_cols = randint(colmin, colmax)
    n_rows = randint(rowmin, rowmax)
    n_bonus = randint(bonus, 2 * bonus)
    
    file = open(filename, 'w')
    file.write(f'{n_bonus}\n')
    bonus_points = list()

    
    for i in range(n_bonus):
        while True:
            x = randint(1, n_cols-2)            
            y = randint(1, n_rows-2)
            cur_point = point(x, y)
            
            used = False
    
            for p in bonus_points:
                if cur_point == p:
                    used = True
                    break
                            
            if used == False:
                bonus = randint(-10, -4)
                bonus_points.append(cur_point)
                file.write(f'{y} {x} {bonus}\n')
                break


    if teleport == True:
        while True:
            gate1 = point(randint(1, n_cols-2), randint(1, n_rows-2))
            gate2 = point(randint(1, n_cols-2), randint(1, n_rows-2))

            if gate1 == gate2:
                continue

            used = False
            for p in bonus_points:
                if (p == gate1) or (p == gate2):
                    used = True
                    break
            
            if used == False:
                break
                    
        
    end = point(int(choice(['0', f'{n_cols-1}'])), randint(1, n_rows-1))
    while True:
        start = point(randint(1, n_cols-2), randint(1, n_rows-2))
        if start == gate1 or start == gate2:
            continue
        else:
            break

    
    for i in range(n_rows):

        if i == 0 or i == n_rows - 1:
            for j in range(n_cols):
                file.write('x')
            file.write('\n')
        else:
            for j in range(n_cols):
                if teleport == True:
                    if gate1.x == j and gate1.y == i:
                        file.write('i')
                        continue
                    elif gate2.x == j and gate2.y == i:
                        file.write('i')
                        continue

                if j == 0 or j == n_cols-1:
                    if i == end.y and j == end.x:
                        file.write(' ')
                    else:
                        file.write('x')
                else:
                    is_bonus_point = False
                    for p in bonus_points:
                        if p.x == j and p.y == i:
                            is_bonus_point = True
                            break

                    if is_bonus_point == True:
                        file.write('+')
                    
                    elif i == start.y and j == start.x:
                        file.write('S')

                    else:
                        file.write(choice(['x', ' ', ' ', ' ']))

            file.write('\n')


    if teleport == True:
        file.write(f'{gate1.y} {gate1.x} ')
        file.write(f'{gate2.y} {gate2.x}\n')

    file.close()

    file = open(filename, 'r')
    maze = file.read()
    file.close()
    print(maze)