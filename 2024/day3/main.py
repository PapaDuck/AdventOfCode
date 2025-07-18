import re
Testing = False

def load_data(test_file=False):
    filename = "input_test2.txt" if test_file else "input.txt"
    with open(filename) as input_file:
        data = input_file.read()
    return data

def split_data(data):
    do_part = []
    data = data.split('don\'t()')
    do_part.append(data[0])
    for dont_data_part in data[1:]:
        dont_data_part = dont_data_part.split('do()')
        if len(dont_data_part) == 2:
            do_part.append(dont_data_part[1])
    # print(do_part)
    do_data_part = ''.join(do_part)
    return do_data_part

def find_pattern(data):
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    # print(matches)
    return matches

def calc_numbers(pattern):
    results = []
    for patter in pattern:
        numbers = re.findall(r"\d{1,3}", patter)
        numbers = [ int(x) for x in numbers ]
        x, y = numbers
        results.append(x*y)
    return results

def day3():
    data = load_data(Testing)
    matches = find_pattern(data)
    results = calc_numbers(matches)
    return sum(results)

def day3part2():
    data = load_data(Testing)
    data = split_data(data)
    matches = find_pattern(data)
    results = calc_numbers(matches)
    return sum(results)


def main():
    print('Exercise 1:', day3())
    print('Exercise 2:', day3part2())

if __name__ == "__main__":
    main()
