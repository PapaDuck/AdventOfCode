import sys

def load_data(test_file=False):
    filename = "input_test.txt" if test_file else "input.txt"
    with open(filename) as input_file:
        data = input_file.read()
    return data.splitlines()


def day22():
    data = load_data(testing)
    print(data)
    # TODO: Implementiere die Lösung hier


def main():
    result = day22()
    print(f'##### {result} #####')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        parameter = sys.argv[1]
        if parameter == "test":
            testing = True
    else:
        testing = False
    main()
