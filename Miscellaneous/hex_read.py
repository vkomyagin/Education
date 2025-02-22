# Read hex dump from old soviet magazines (Radio etc) pdf
# there should be 16 2-symbols chunks in line
# these chunks covert to bytes



hex_conversion = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                  'l': 1, 'O': 0, 'Б': 6, 'В': 11, 'S': 5, 'I': 1,
                  'З': 3, 'Е': 14, 'А': 10, 'С': 12, 'О': 0, 'P': 15, 'Р': 15}


def convert_symbol(s: str) -> int:
    try:
        if s <= '9':
            r = int(s)
        else:
            r = hex_conversion[s]
    except:
        print('cannot convert', s)
        r = 0
    return r


def convert_chunk(c: str) -> int:
    return convert_symbol(c[0]) * 16 + convert_symbol(c[1])

if __name__ == '__main__':

    F = 'nc.txt'
    NAME = 'NC      '

    f = open(F, encoding='utf-8')
    res = bytearray()

    for lin in f:
        ls = lin.split()
        i = 0
        while i < len(ls):
            if len(ls(i)) != 2:
                ls.pop(i)
            else:
                i += 1
        if len(ls) != 16:
            continue
        for c in ls:
            res.append(convert_chunk(c))

    # get ORDOS header
    res_header = bytearray()
    for s in NAME: # name
        res_header.append(ord(s))
    res_header.append(0)  # start bytes
    res_header.append(0)
    res_header.append(len(res) % 16) # length bytes
    res_header.append(len(res) // 16)
    for _ in range(4):  # addition to 16 bytes
        res_header.append(0)

    f.close()
    fb = open(F.split('.')[0] + '.hex', 'wb')
    fb.write(res_header)
    fb.write(res)
    fb.close()
