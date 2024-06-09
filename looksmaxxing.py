import sys
import re

def parse_input():
    supermarket = {}
    shopping_lists = []
    current_list = []
    regals_reading = True
    regal_index = 0

    for line in sys.stdin:
        line = line.strip()
        if regals_reading:
            if not line:
                regals_reading = False
                shopping_lists.append(current_list)
                current_list = []
                continue
            
            try:
                match = re.match(r"(\d+):(.+)", line)
                if not match:
                    print("Nespravny vstup.")
                    sys.exit(1)
                
                regal_num = int(match.group(1))
                if regal_num != regal_index:
                    print("Nespravny vstup.")
                    sys.exit(1)
                
                items = match.group(2).strip().split(',')
                for item in items:
                    item = item.strip().lower()
                    if regal_num not in supermarket:
                        supermarket[regal_num] = []
                    supermarket[regal_num].append(item)
                regal_index += 1
            except ValueError:
                print("Nespravny vstup.")
                sys.exit(1)
        else:
            if not line:
                shopping_lists.append(current_list)
                current_list = []
                continue
            current_list.append(line.strip().lower())
    
    if len(supermarket) == 0 or len(shopping_lists) == 0:
        print("Nespravny vstup.")
        sys.exit(1)
    
    if current_list:
        shopping_lists.append(current_list)

    return supermarket, shopping_lists

def find_item(supermarket, item):
    for regal_num, items in supermarket.items():
        for market_item in items:
            if item in market_item:
                return regal_num, market_item
    return None, item

def optimize_shopping_list(supermarket, shopping_list):
    optimized_list = []
    not_found = []

    for item in shopping_list:
        regal_num, found_item = find_item(supermarket, item)
        if regal_num is not None:
            optimized_list.append((regal_num, found_item))
        else:
            not_found.append(item)

    optimized_list.sort(key=lambda x: x[0])
    optimized_list.extend([(None, item) for item in not_found])
    return optimized_list

def main():
    supermarket, shopping_lists = parse_input()
    
    for shopping_list in shopping_lists:
        optimized_list = optimize_shopping_list(supermarket, shopping_list)
        for regal_num, item in optimized_list:
            if regal_num is not None:
                print(f"{regal_num}: {item}")
            else:
                print(f"Not found: {item}")
        print()

if __name__ == "__main__":
    main()
