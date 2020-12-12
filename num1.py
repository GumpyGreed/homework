def count (h):
    counterup = 0
    counterlow = 0
    for i in range(len(h)):
        if h[i].upper() == h[i]:
            counterup += 1
        elif h[i] == ' ':
            pass
        else:
            counterlow += 1
    print(counterup)
    print(counterlow)


def user_input():
    return str(input())




def prog ():
    strr = user_input() 
    count(strr)

prog()
