import hashlib

# encoding GeeksforGeeks using md5 hash
# function 

def day4(anzahl_nullen):
    """Tag 4 des Jahres 2015"""
    with open('./input.txt') as input_file:
        input = input_file.read()
    
    number = 0
    input = 'ckczppom'
    result = True
    while result:
        test = input+str(number)
        print(test)
        result = hashlib.md5(test.encode()).hexdigest()
        if result[:anzahl_nullen] == anzahl_nullen*'0':
            result = False
        number+=1
    print(test)

def main():
    anzahl_nullen = input('Wieviele :')
    day4(anzahl_nullen)

if __name__ == "__main__":
    main()
