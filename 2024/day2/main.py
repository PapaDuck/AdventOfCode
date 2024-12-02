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
        
        errors = 0
        safe = False
        
        differences = [j-i for i, j in zip(level[:-1], level[1:])]

        pos = [i for i in differences if i > 0]
        neg = [i for i in differences if i < 0]
        if len(pos) == 0 or len(neg) == 0:
            safe = True
        
        for dif in differences:
            if dif < 0:
                dif = dif*-1
            if dif >= min_difference and dif <= max_difference:
                safe = True
            else:
                safe = False
                print(f'{dif} | {min_difference}-{max_difference}')
                break
        
        print(level, safe)
        report_list.append(safe)

        continue
        # Test Difference
        for i in dif:
                if dif < 0:
                    dif = dif*-1
                
                # Test if Tolarance
                if dif < min_difference or dif > max_difference:
                    errors += 1
                    print(f'Error {dif} zwischen {min_difference}-{max_difference}')

       

        if errors <= tolarate_lvl and safe:
            report_list.append('safe')
            print(f'safe: {report} | {errors}')
        else:
            report_list.append('unsafe')
            print(f'unsafe: {report} | {errors}')

    print('----------- ',report_list.count(True))
    return


def main():
    day2()

if __name__ == "__main__":
    main()
