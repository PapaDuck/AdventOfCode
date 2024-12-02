def day2():
    """Tag 2 des Jahres 2015"""
    with open('./input.txt') as input_file:
        wrapping_paper = input_file.read()
    
    presents = wrapping_paper.split('\n')[:-1]

    sum_area = 0
    sum_ribbon = 0

    for present in presents:
        length, width, height = present.split('x')
        length = int(length)
        width = int(width)
        height = int(height)
        present = [length, width, height]
        present.sort()

        # wrap
        side1 = length*width
        side2 = width*height
        side3 = height*length
        surface_area = (2*side1+2*side2+2*side3)+min(side1,side2,side3)
        sum_area += surface_area

        # ribbon
        ribbon = (present[0]*2)+(present[1]*2)+(length*width*height)
        sum_ribbon += ribbon
    return sum_area, sum_ribbon


def main():
    surface_area, ribbon = day2()
    print('Surface Area:',surface_area)
    print('Ribbon:',ribbon)

if __name__ == "__main__":
    main()
