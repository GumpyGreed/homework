def builder (h):
    p = h//2
    for i in range(p):
        print ('*' * (i+1))
    print('*' * (p+1))
    i = h//2
    while i > 0:
        print ('*' * (i))
        i -= 1
def user_input():
    return int(input())
def prog ():
    num = user_input()
    if num % 2 == 0:
        print('Введите нечетное число')
    else:
        builder(num)

prog()