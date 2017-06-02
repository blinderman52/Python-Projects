# read file
def read_file():
    file = open('MLB.csv')
    sum = 0
    count = -1
    for line in file:
        player = line.split(',')
        print('%-25s %3s' % (player[1], player[3]))
        if count >= 0:
            sum += float(player[3])
        count += 1
    result = sum/count
    return result


# === Main ===

create = read_file()
print('%-25s %7s' % ('Average:', create))


