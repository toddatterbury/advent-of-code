

def find_duplicate_item(first_compartment, second_compartment):
    for (index, item) in enumerate(first_compartment):
        if item in second_compartment:
            return item


def get_priority(item):
    if item.islower():
        priority = ord(item) - 96
    else:
        priority = ord(item) - 64 + 26
    return priority


def calculate_priorities(filename):

    with open('input.txt') as f:
        lines = f.readlines()

    total_priority = 0
    for line in lines:

        length = len(line)
        first_compartment = line[:int(length/2)]
        second_compartment = line[int(length/2):]

        item = find_duplicate_item(first_compartment, second_compartment)
        priority = get_priority(item)
        total_priority += priority

    return total_priority


def find_common_badge(elf1, elf2, elf3):
    print(elf1)
    print(elf2)
    print(elf3)
    for item in elf1:
        if item in elf2 and item in elf3:
            return item


def calculate_priorities_of_elfs(filename):

    with open('input.txt') as f:
        lines = f.readlines()

    total_priority = 0
    for moving_index in range(int(len(lines)/3)):
        elf1, elf2, elf3 = lines[3*moving_index:(3*moving_index)+3]
        item = find_common_badge(elf1, elf2, elf3)
        priority = get_priority(item)
        total_priority += priority

    return total_priority


if __name__ == '__main__':
    print("===============")
    print("Advent of Code")
    print("     Day 3    ")
    print("===============\n")

    total_priority = calculate_priorities_of_elfs("input.txt")
    print("Total: ", total_priority)
