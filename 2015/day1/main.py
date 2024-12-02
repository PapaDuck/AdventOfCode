def day1():
    """Tag 1 des Jahres 2015"""
    with open('./input.txt') as input_file:
        apartment_floors = input_file.read()

    first_basement = False
    position = 0
    floor = 0
    for direction in apartment_floors:
        position += 1

        if direction=='(':
            floor+=1
        elif direction==')':
            floor-=1
        else:
            continue
        if first_basement == False and floor < 0:
            print('First Basement:', position)
            first_basement = True
    print(floor)


def main():
    print('Die Lösung ist:')
    day1()

if __name__ == "__main__":
    main()
