def day2():
    """Tag 2 des Jahres 2024"""
    with open('./input.txt') as input_file:
        data = input_file.read()
    tolarate_lvl = int(input('Tolenrance: '))
    data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

    reports = data.splitlines()

    max_difference = 3
    min_difference = 1

    report_list = []

    for report in reports:
        level = report.split(' ')
        level = [ int(x) for x in level ]

        safe = True

        # TOL LEVEL
        level_bu = level.copy()
        for i in range(len(level)-tolarate_lvl):
            level = level_bu.copy()
            if tolarate_lvl != 0:
                print('vor', level)
                del level[i]
                print('nach', level)


            differences = [j-i for i, j in zip(level[:-1], level[1:])]

            # Auf oder Absteigend
            pos = [i for i in differences if i > 0]
            neg = [i for i in differences if i < 0]
            if len(pos) != 0 and len(neg) != 0:
                safe = False

            # In Range
            for dif in differences:
                if dif < 0:
                    dif = dif*-1
                if dif < min_difference or dif > max_difference:
                    safe = False

            # Reihenfolge
            for i, lev in enumerate(level):
                if i > 0:
                    if (level[i] > level[i-1] and len(neg) != 0):
                        safe = False
                    if (level[i] < level[i-1] and len(pos) != 0):
                        safe = False
            print(level, safe)
            report_list.append(safe)

    print('----------=== ',report_list.count(True))
    return


def main():
    day2()

if __name__ == "__main__":
    main()
