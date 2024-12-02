def day3():
    """Tag 3 des Jahres 2015"""
    with open('./input.txt') as input_file:
        coordinates = input_file.read()

    x_pos = 0
    y_pos = 0
    number = 0
    house = {f'{x_pos}.{y_pos}' : 1}

    for direction in coordinates:
        if direction == '^':
            y_pos += 1
        elif  direction == 'v':
            y_pos -= 1
        elif  direction == '>':
            x_pos += 1
        elif  direction == '<':
            x_pos -= 1
        if f'{x_pos}.{y_pos}' in house.keys():
            house[f'{x_pos}.{y_pos}'] += 1
        else:
            house[f'{x_pos}.{y_pos}'] = 1
    return house

def count_houses(houses):
    houses_with_presents = 0
    for pos, presents in houses.items():
        if presents > 0:
            houses_with_presents += 1
    return houses_with_presents

def robo_santa():
    with open('./input.txt') as input_file:
        coordinates = input_file.read()

    robo = 0
    x_pos_santa = 0
    y_pos_santa = 0
    x_pos_robo = 0
    y_pos_robo = 0
    number = 0
    house = {f'{x_pos_santa}.{y_pos_santa}' : 1}

    for direction in coordinates:
        if direction == '^':
            if robo % 2:
                y_pos_santa += 1
            else:
                y_pos_robo += 1
        elif  direction == 'v':
            if robo % 2:
                y_pos_santa -= 1
            else:
                y_pos_robo -= 1
        elif  direction == '>':
            if robo % 2:
                x_pos_santa += 1
            else:
                x_pos_robo += 1
        elif  direction == '<':
            if robo % 2:
                x_pos_santa -= 1
            else:
                x_pos_robo -= 1

        if robo % 2:
            if f'{x_pos_santa}.{y_pos_santa}' in house.keys():
                house[f'{x_pos_santa}.{y_pos_santa}'] += 1
            else:
                house[f'{x_pos_santa}.{y_pos_santa}'] = 1
        else:
            if f'{x_pos_robo}.{y_pos_robo}' in house.keys():
                house[f'{x_pos_robo}.{y_pos_robo}'] += 1
            else:
                house[f'{x_pos_robo}.{y_pos_robo}'] = 1
        robo += 1
    return house


def main():
    houses = day3()
    houses_with_presents = count_houses(houses)
    print('Santa: ',houses_with_presents)

    robo_houses = robo_santa()
    houses_with_presents = count_houses(robo_houses)
    print('Santa+Robo: ',houses_with_presents)

if __name__ == "__main__":
    main()
