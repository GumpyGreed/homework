# def get_strintg(strr):
#     strr.lower()
#     tmp = []
#     for i in strr:
#         k = 0
#         for j in strr:
#             if strr[i] == strr[j]:
#                 k += 1
#         tmp.append(strr[i] + ':' + ('*' * k))

# print(get_strintg('Moscow'))
            
def get_str(town):
    st = ''
    town = ''.join(town.lower().split())
    for i in town:
        if i not in st:
            st += i + ':' + '*' * town.count(i) + ','
    return st[:-1]

print(get_str('Moscow'))