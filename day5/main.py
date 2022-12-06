import re


def calculate_stacks(filename):

    with open('input.txt') as f:
        lines = f.readlines()
        print(lines)

    new_line_split = lines.index('\n')
    stack_structure = lines[:new_line_split-1]
    moves_structure = lines[new_line_split+1:]

    stacks = [[] for i in range(9)]
    stack_indices = []
    stack_index_structure = lines[new_line_split-1:new_line_split][0]

    stack_number = 1
    for index, ch in enumerate(stack_index_structure):
        if ch == str(stack_number):
            stack_indices.append(index)
            stack_number += 1

    # Build stacks
    stack_structure.reverse()
    for stack_line in stack_structure:

        for index, ch in enumerate(stack_line):

            if ch != ' ' and ch != '[' and ch != ']' and ch != '\n':
                # Add to correct stack
                index_of_stack = stack_indices.index(index)
                stacks[index_of_stack].append(ch)


    moves = []
    for mv in moves_structure:

        # GET MOVES
        number_of_items, from_stack, to_stack = re.findall(r'\d+', mv)
        new_move = {
            'number_of_items': int(number_of_items),
            'from_stack': int(from_stack),
            'to_stack': int(to_stack),
        }
        moves.append(new_move)

        # Part 1
        # for i in range(new_move['number_of_items']):
        #     item_to_move = stacks[new_move['from_stack']-1].pop(-1)
        #     stacks[new_move['to_stack']-1].append(item_to_move)

        # Part 2
        items_to_move = []

        # Get items of stack
        for i in range(new_move['number_of_items']):
            item_to_move = stacks[new_move['from_stack']-1].pop(-1)
            items_to_move.append(item_to_move)

        # Put items back on stack
        items_to_move.reverse()
        for i in range(new_move['number_of_items']):
            stacks[new_move['to_stack']-1].append(items_to_move[i])


    top_of_stacks = ""
    for stack in stacks:
        top_of_stacks += stack[-1]

    return top_of_stacks


if __name__ == '__main__':
    print("===============")
    print("Advent of Code")
    print("     Day 5    ")
    print("===============\n")

    top_of_stacks = calculate_stacks("input.txt")
    print("Top of stacks: ", top_of_stacks)
