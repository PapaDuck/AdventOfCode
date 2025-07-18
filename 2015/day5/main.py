def day5():
    """Tag 5 des Jahres 2015"""
    alpha = "abcdefghijklmnopqrstuvwxyz"

    with open('./test.txt') as input_file:
        data = input_file.read()
    strings = data.splitlines()

    def contain_vowels(string, nr):
        vowels = "aeiou"
        nr_of_vowels = 0
        for char in string:
            if char in vowels:
                nr_of_vowels += 1
        if nr_of_vowels >= nr:
            return True
        else:
            return False
    
    def letter_in_rows(string, nr_of_letter_in_row):
        print(string)
        # uni_chars = list(string)
        uni_chars = list(dict.fromkeys(list(string)))
        print(uni_chars)
        for uni_char in uni_chars:
            if string.count(uni_char) < 2:
                print(uni_char, False)
                uni_chars.remove(uni_char)
            else:
                print(uni_char, "##########")
        print(uni_chars)
    for string in strings:
        vowel = contain_vowels(string, 3)
        lir = letter_in_rows(string, 1)

def main():
    day5()

if __name__ == "__main__":
    main()
