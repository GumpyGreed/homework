code_dict = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
decode_dict = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}

def encode(strr):
    t = ''
    for i in strr:
        if i in code_dict:
            t += str(code_dict[i])
        else:
            t += i
    return t

def decode(strr):
    t = ''
    for i in strr:
        if i in decode_dict:
            t += decode_dict[i]
        else:
            t += i
    return t

print(encode('hello'))
