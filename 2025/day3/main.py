import sys

def load_data(test_file=False):
    filename = "input_test.txt" if test_file else "input.txt"
    with open(filename) as input_file:
        data = input_file.read()
    return data.splitlines()

def high_battery(bank: str) -> int:
    highest_battery = 0
    for pos_one, battery_one in enumerate(bank[:-1]):
        for pos_two, battery_two in enumerate(bank[1:]):
            if pos_one-1 == pos_two or pos_one-1>=pos_two:
                continue
            battery = int(battery_one+battery_two)
            if battery > highest_battery:
                highest_battery = battery
    return highest_battery


def day3():
    sum_battery = 0
    data = load_data(testing)
    for bank in data:
        print(bank)
        win = high_battery(bank)
        sum_battery += win
    return sum_battery

def main():
    result = day3()
    print(f'##### {result} #####')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        parameter = sys.argv[1]
        if parameter == "test":
            testing = True
    else:
        testing = False
    main()
