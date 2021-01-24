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

def prog ():
    game = True
    num = user_input_field()
    position = start_location(field_builder(num))
    field_condition(position)

    while game:
        user_characteristic = user_input()

        if user_characteristic == 'up':
            position = move_up(position)
        if user_characteristic == 'left':
            position = move_left(position)
        if user_characteristic == 'down':
            position = move_down(position)
        if user_characteristic == 'right':
            position = move_right(position)
        if user_characteristic == 'exit':
            game = False
        if game:
            field_condition(position)

prog()