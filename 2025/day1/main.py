import sys

def load_data(test_file=False):
    filename = "input_test.txt" if test_file else "input.txt"
    with open(filename) as input_file:
        data = input_file.read()
    return data.splitlines()


def split_code(code: str) -> list:
    direction = code[:1]
    number = int(code[1:])
    return [direction, number]


def recalc(dial: int) -> int:
    while dial < 0:
        dial += 100
    while dial > 99:
        dial -= 100
    return dial


def day1():
    data = load_data(testing)

    start = 50
    nulls = 0

    for step in data:
        new_start = start
        direction, number = split_code(step)

        if direction == 'L':
            new_start -= number
        elif direction == 'R':
            new_start += number

        new_start = recalc(new_start)

        if new_start == 0:
            nulls += 1
        print(f'x: {start} - {step} -> {new_start}')
        start = new_start
    return nulls


def main():
    result = day1()
    print(f'##### {result} #####')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        parameter = sys.argv[1]
        if parameter == "test":
            testing = True
    else:
        testing = False
    main()
