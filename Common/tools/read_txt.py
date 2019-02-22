# 读取txt格式文件
def read_txt(file):
    L = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            if line[-1] == "\n":
                line = line[:-1]
            if line == '':
                continue
            if line[0] == "#":
                continue
            L.append(line.split("|"))
    return L
