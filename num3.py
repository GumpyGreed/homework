def builder (n):
    for i in range(n):
        print(str(i + 1) * (i + 1))

def user_input():
    return int(input())

def prog():
    num = user_input()
    builder(num)
prog()