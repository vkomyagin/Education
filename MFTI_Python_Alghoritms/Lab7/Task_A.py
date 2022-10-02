# 0 вес грузовика без груза,
# 1 высота платформы кузова (на которой стоят грузы),
# 2 вес пианино (мост),
# 3 высота пианино,
# 4 вес холодильника,
# 5 высота холодильника (туннель),
# 6 максимальный допустимый вес на мосту,
# 7 максимальная допустимая высота в туннеле

def check_bridge(weight, max_weight):
    return weight <= max_weight


def check_tunnel(height, max_height):
    return height <= max_height


if __name__ == '__main__':
    d = list()
    for _ in range(8):
        d.append(int(input()))

    if check_bridge(d[0] + d[2] + d[4], d[6]):
        if check_tunnel(d[1] + d[5], d[7]):
            print('YES')
        else:
            print('NO')
    elif check_tunnel(max(d[1] + d[3], d[1] + d[5]), d[7]):
        if check_bridge(d[0] + d[2], d[6]):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
