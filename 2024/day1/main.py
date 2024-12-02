def day1():
    """Tag 1 des Jahres 2024"""
    with open('./input.txt') as input_file:
        location_ids = input_file.read()

    
    left_list = []
    right_list = []
    distances = []

    single_location_ids = location_ids.splitlines()

    for location_id in single_location_ids:
        left, right = location_id.split('   ')
        left_list.append(int(left))
        right_list.append(int(right))

    left_list_clean = left_list
    right_list_clean = right_list
    left_list_clean.sort()
    right_list_clean.sort()

    for index in range(len(min(right_list_clean, left_list_clean))):
        small = min(right_list_clean[index],left_list_clean[index])
        big = max(right_list_clean[index],left_list_clean[index])
        distance = big-small
        distances.append(distance)
    print(sum(distances))

    # part 2
    similarity_score = 0
    for index in range(len(min(right_list, left_list))):
        left = left_list[index]
        in_right = sum(left == i for i in right_list)
        similarity = left*in_right
        print(f'{left} in r_l = {in_right} | sim={similarity}')

        similarity_score += similarity
    print(similarity_score)


    return
def main():
    day1()
    
if __name__ == "__main__":
    main()
