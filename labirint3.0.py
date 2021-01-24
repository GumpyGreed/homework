from random import random

def user_input_field():
    return int(input())

def user_input():
    return input()

def field_builder(n):
    """ output: field, for example:
    input: 3
    [['_','_','_'],
    ['_','_','_'],
    ['_','_','_']]
    """
    tmp = []
    tmp_2 = []
    for i in range(n):
        tmp.append('_')
    for i in range(n):
        tmp_2.append(tmp[:])
    return(tmp_2)

def start_location(f):
    """set start location of x (x - player)
    """
    f[0][0] = 'x'
    return f

def move_left (f):
    """ move 'x' in left on field
    """
    tmp_moved = f[:]
    for k in range(len(f)):
        for l in range(len(f)):
            if f[k][l] == 'x':
                tmp_moved[k][l] = '_'
                if l == 0:
                    tmp_moved[k][len(f)-1] = 'x'
                else:
                    tmp_moved[k][l-1] = 'x'
                break
    return tmp_moved

def move_right (f):
    """ move 'x' in right on field
    """
    tmp_moved = f[:]
    for k in range(len(f)):
        for l in range(len(f)):
            if f[k][l] == 'x':
                tmp_moved[k][l] = '_'
                if l == len(f)-1:
                    tmp_moved[k][0] = 'x'
                else:
                    tmp_moved[k][l+1] = 'x'
                break
    return tmp_moved

def move_up (f):
    """ move 'x' in up on field
    """
    tmp_moved = f[:]
    for k in range(len(f)):
        for l in range(len(f)):
            if f[k][l] == 'x':
                tmp_moved[k][l] = '_'
                if k == 0:
                    tmp_moved[(len(f)-1)][l] = 'x'
                else:
                    tmp_moved[k-1][l] = 'x'
                return tmp_moved
    return

def move_down (f):
    """ move 'x' in down on field
    """
    tmp_moved = f[:]
    for k in range(len(f)):
        for l in range(len(f)):
            if f[k][l] == 'x':
                tmp_moved[k][l] = '_'
                if k == len(f)-1:
                    tmp_moved[0][l] = 'x'
                else:
                    tmp_moved[k+1][l] = 'x'
                return tmp_moved
    return

def field_condition(f):
    """
    input: field size
    output: show field with 'x'
    """
    for j in f:
        print(''.join(j))

def add_block(f, block):
    """
    input: field size, block_quantity 
    output: field with block
    """
    field_lenght = range(len(f))
    block_percent = block/100
    for i in field_lenght:
        for j in field_lenght:
            if random() <= block_percent and f[i][j] != 'x':
                f[i][j] = 'o'

def find_pos(f):
    pos_x = 0
    pos_y = 0
    field_lenght = range(len(f))

    for x in field_lenght:
        for y in field_lenght:
            if f[x][y] == 'x':
                pos_x = x
                pos_y = y
                break
    
    return pos_x, pos_y

def check_block(com, f, pos):
    x, y = pos
    flag = False
    if com == 'up':
        if f[x-1][y] == 'o':
            flag = True
    elif com == 'right':
        if y+1 > len(f)-1:
            if f[x][0] == 'o':
                flag = True
        else:
            if f[x][y+1] == 'o':
                flag = True
    elif com == 'down':
        if x+1 > len(f)-1:
            if f[0][y] == 'o':
                flag = True
        else:
            if f[x+1][y] == 'o':
                flag = True
    elif com == 'left':
        if f[x][y-1] == 'o':
            flag = True
    return flag

def block_despetcher(com, f, pos):
    block = check_block(com, f, pos)

    if com == 'up' and not block:
        f = move_up(f, pos)
    elif com == 'right' and not block:
        f = move_right(f, pos)
    elif com == 'down' and not block:
        f = move_down(f, pos)
    elif com == 'left' and not block:
        f = move_left(f, pos)
    else:
        print('Oops, this move not avaliable')
    return f

def prog ():
    game = True
    num = user_input_field()
    position = start_location(field_builder(num))
    add_block(position, 40)
    field_condition(position)

    while game:
        user_characteristic = user_input()
        player_pos = find_pos(position)
        position = block_despetcher(user_characteristic, position, player_pos)

        if user_characteristic == 'exit':
            game = False
        if game:
            field_condition(position)

prog()