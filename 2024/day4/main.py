def load_data(test_file=False):
    filename = "input_test.txt" if test_file else "input.txt"
    with open(filename) as input_file:
        data = input_file.read()
    return data

def split_data_grid(data):
    grid_data = []
    data = data.splitlines()
    for line in data:
        grid_data.append(list(line))
    return grid_data

def search_word(word, data):
    result = 0
    # horizontal+rev
    for line in data:
        words = ''.join(line).count(word)
        result += words
        words = ''.join(line)[::-1].count(word)
        result += words
    hor = result
    #print('hor + rev',hor)
    # vertical+rev
    for x, char_x in enumerate(data[0]):
        vertical = []
        for y, char_y in enumerate(data):
            vertical.append(data[y][x])
        vertical = ''.join(vertical)
        words = vertical.count(word)
        result += words
        words = vertical[::-1].count(word)
        result += words
    ver = result
    #print('ver + rev',ver-hor)
    # diagonal LU-RL+rev
    x_len = len(data[0])
    y_len = len(data)
    for x in range(x_len):
        diagonal = []
        for y in range(y_len):
            if y <= (y_len-(len(word)-x)):
                if x <= (x_len-(len(word)-y)):
                    diagonal.append(data[x][y])
                    #for i in range(len(word)):
                        #diagonal = ''
                        #diagonal.append(data[x+i][y+i])
        #print(diagonal)
        diagonal = ''.join(diagonal)
        words = diagonal.count(word)
        result += words
        words = diagonal[::-1].count(word)
        result += words
    dia1 = result
    print('dia1 + rev',dia1-ver)
    # diagonal LL-RU+rev
    for x in range(x_len):
        diagonal = []
        for y in range(y_len):
            if y >= (len(word)-x):
                if x >= (len(word)-y): # <----------- HERE
                    print('x',x,'y', y)
                    diagonal.append(data[x][y])
                    #for i in range(len(word)):
                        #diagonal = ''
                        #diagonal.append(data[x+i][y+i])
        #print(diagonal)
        diagonal = ''.join(diagonal)
        words = diagonal.count(word)
        result += words
        words = diagonal[::-1].count(word)
        result += words
    dia2 = result
    #print('dia2 + rev',dia2-dia1)
    return result

def day4():
    """Tag 4 des Jahres 2024"""
    testing = True
    data = load_data(testing)
    data = split_data_grid(data)
    words = search_word('XMAS',data)
    print('+++++++')
    if words == 18:
        print('YEEEEEEEEES')
        print('Ergebnis 1:', words)

def main():
    day4()

if __name__ == "__main__":
    main()
