def load_data(test_file=False):
    filename = "input_test.txt" if test_file else "input.txt"
    with open(filename) as input_file:
        data = input_file.read()
    rules, page_updates = data.split('\n\n')
    return rules, page_updates

def prep_data(rules, page_updates):
    rules_list = []
    rules = rules.splitlines()
    page_updates = page_updates.splitlines()
    for rule in rules:
        from_page, to_page = rule.split('|')
        from_page = int(from_page)
        to_page = int(to_page)
        rules_list.append([from_page, to_page])

    page_updates_list = []
    for pages in page_updates:
        pages = pages.split(',')
        pages = [ int(x) for x in pages ]
        page_dict = {}
        for id, page in enumerate(pages):
            page_dict[id]=page
        page_updates_list.append(page_dict)

    return rules_list, page_updates_list

# <--------- HERE
def test_rule(rules, pages_dict):
    pages = len(pages_dict.values())
    rules_correct = True
    befor = []
    for id, page in pages_dict.items():
        after = list(pages_dict.values())[list(pages_dict.keys()).index(id) + 1:]
        pre = [rule for rule in rules if rule[0] == page]
        post = [rule for rule in rules if rule[1] == page]
        # <---- insert RULE here
        print(id, page)
        befor.append(page)
    return rules_correct

def order_test(rules, updates):
    first_row = True
    for update in updates:
        if first_row: # für test der ersten row
            test_rule(rules, update)

            first_row = False # für test der ersten row

def day5():
    testing = True
    rules, page_updates = load_data(testing)
    rules, page_updates = prep_data(rules, page_updates)
    order_test(rules, page_updates)
    #print(x)


def main():
    day5()

if __name__ == "__main__":
    main()
