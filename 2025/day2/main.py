import sys


def load_data(test_file=False):
    filename = "input_test.txt" if test_file else "input.txt"
    with open(filename) as input_file:
        data = input_file.read()
    return data.splitlines()


def splitFile(data: str) -> list:
    id_range = data[0].split(',')
    return id_range

def test_id(id: int) -> bool:
    id_string = str(id)
    if len(id_string) % 2 == 0:
        if id_string[:int(len(id_string)/2)] == id_string[int(len(id_string)/2):]:
            return True

def day2():
    id_sum = 0
    data = load_data(testing)
    id_ranges = splitFile(data)
    for id_range in id_ranges:
        id_start, id_end = id_range.split('-')
        id_start = int(id_start)
        id_end = int(id_end)
        for id in range(id_start, id_end+1):
            if test_id(id):
                id_sum += id
    return id_sum


def main():
    result = day2()
    print(f'##### {result} #####')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        parameter = sys.argv[1]
        if parameter == "test":
            testing = True
    else:
        testing = False
    main()
