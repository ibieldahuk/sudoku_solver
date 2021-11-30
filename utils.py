def print_game(s_list):
    for r in range(len(s_list)):
        for c in range(len(s_list[r])):
            print(s_list[r][c], end='  ')
        print('')

def find_empty_spot(s_list):
    for r in range(len(s_list)):
        for c in range(len(s_list[r])):
            if s_list[r][c] == 0:
                return [r, c]
    return None

def get_block(row, col):
    if row < 3 and col < 3:
        return 0
    if row < 3 and 2 < col < 6:
        return 1
    if row < 3 and 5 < col:
        return 2
    if 2 < row < 6 and col < 3:
        return 3
    if 2 < row < 6 and 2 < col < 6:
        return 4
    if 2 < row < 6 and 5 < col:
        return 5
    if 5 < row and col < 3:
        return 6
    if 5 < row and 2 < col < 6:
        return 7
    if 5 < row and 5 < col:
        return 8

def is_compatible(s_list, b_list, value, coords):
    row = coords[0]
    col = coords[1]
    if not is_compatible_w_row(s_list, value, row):
        return False
    if not is_compatible_w_col(s_list, value, col):
        return False
    if not is_compatible_w_block(b_list, value, row, col):
        return False
    return True

def is_compatible_w_row(s_list, value, row):
    for i in s_list[row]:
        if i == value:
            return False
    return True

def is_compatible_w_col(s_list, value, col):
    for i in s_list:
        if i[col] == value:
            return False
    return True

def is_compatible_w_block(b_list, value, row, col):
    index = get_block(row, col)
    if value in b_list[index]:
        return False
    return True

def solve(s_list, b_list):
    # Get empty spots.
    empty_coords = find_empty_spot(s_list)

    #Check that there are no empty spots.
    if empty_coords is None:
        return True

    else:

        #Try each value.
        for x in range(1, 10):
            #If it is a possible value,
            if is_compatible(s_list, b_list, x, empty_coords):
                #place it,
                s_list[empty_coords[0]][empty_coords[1]] = x
                block_i = get_block(empty_coords[0], empty_coords[1])
                b_list[block_i].append(x)
                #and start over.
                if solve(s_list, b_list):
                    return True
                b_list[block_i].pop()
        #If no values where possible,
        #Set its values to 0
        s_list[empty_coords[0]][empty_coords[1]] = 0
        #and return false.
        return False