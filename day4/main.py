
def calculate_fully_contained_pairs(filenme):


    with open('input.txt') as f:
        lines = f.readlines()

    total_pairs = 0
    for line in lines:
        range1_values, range2_values = line.split(',')[0], line.split(',')[1]

        range1_start, range1_end = int(range1_values.split('-')[0]), int(range1_values.split('-')[1])
        range2_start, range2_end = int(range2_values.split('-')[0]), int(range2_values.split('-')[1])

        # Create range objects
        range1 = range(range1_start, range1_end+1)
        range2 = range(range2_start, range2_end+1)

        if len(range1) < len(range2):
            if range1_start in range2 or range1_end in range2:
                total_pairs += 1
        else:
            if range2_start in range1 or range2_end in range1:
                total_pairs += 1

    return total_pairs


if __name__ == '__main__':
    print("===============")
    print("Advent of Code")
    print("     Day 4    ")
    print("===============\n")

    total_pairs = calculate_fully_contained_pairs("input.txt")
    print("Total: ", total_pairs)