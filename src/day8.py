with open('data/day8.txt') as f:
    grid = []
    for line in f.readlines():
        grid.append([int(tree) for tree in line[:-1]])

def one_star(grid):
    nb_visible = 0
    for c_j in range(len(grid)):
        for c_i in range(len(grid[0])):
            if c_i == 0 or c_i == len(grid[0]) - 1 or c_j == 0 or c_j == len(grid) - 1:
                nb_visible += 1
                continue
            c_t = grid[c_j][c_i]
            # left
            i = c_i
            is_visible = False
            while(i != 0):
                i -= 1
                if grid[c_j][i] < c_t:
                    is_visible = True
                else:
                    is_visible = False
                    break
            if is_visible:
                nb_visible +=1
                continue
            # right
            i = c_i
            is_visible = False
            while(i != len(grid[0]) - 1):
                i += 1
                if grid[c_j][i] < c_t:
                    is_visible = True
                else:
                    is_visible = False
                    break
            if is_visible:
                nb_visible +=1
                continue

            # top
            j = c_j
            is_visible = False
            while(j != 0):
                j -= 1
                if grid[j][c_i] < c_t:
                    is_visible = True
                else:
                    is_visible = False
                    break
            if is_visible:
                nb_visible +=1
                continue

            # bottom
            j = c_j
            is_visible = False
            while(j != len(grid) - 1):
                j += 1
                if grid[j][c_i] < c_t:
                    is_visible = True
                else:
                    is_visible = False
                    break
            if is_visible:
                nb_visible +=1
                continue

    print(nb_visible)


def two_star(grid):
    max_scenic = 0
    for c_j in range(len(grid)):
        for c_i in range(len(grid[0])):
            if c_i == 0 or c_i == len(grid[0]) - 1 or c_j == 0 or c_j == len(grid) - 1:
                continue
            c_t = grid[c_j][c_i]
            # left
            i = c_i
            l_scenic = 0
            while(i != 0):
                i -= 1
                l_scenic +=1
                if grid[c_j][i] >= c_t:
                    break
            # right
            i = c_i
            r_scenic = 0
            while(i != len(grid[0]) - 1):
                i += 1
                r_scenic += 1
                if grid[c_j][i] >= c_t:
                    break

            # top
            j = c_j
            t_scenic = 0
            while(j != 0):
                j -= 1
                t_scenic += 1
                if grid[j][c_i] >= c_t:
                    break

            # bottom
            j = c_j
            b_scenic = 0
            while(j != len(grid) - 1):
                j += 1
                b_scenic +=1
                if grid[j][c_i] >= c_t:
                    break
            cur_scenic =  l_scenic * r_scenic * t_scenic * b_scenic
            if cur_scenic > max_scenic:
                print(f'{c_j}_{c_i} : {l_scenic} * {r_scenic} * {t_scenic} * {b_scenic} = {cur_scenic} ')
                max_scenic = cur_scenic
            
    print(max_scenic)
two_star(grid)
