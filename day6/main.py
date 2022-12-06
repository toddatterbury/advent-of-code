
def calculate_start_of_packet_markers(filename):
    with open('input.txt') as f:
        lines = f.readlines()

    datastream = lines[0]
    print(datastream)

    start_of_package_found = False

    moving_index = 0
    window = ""
    while not start_of_package_found:

        window = datastream[moving_index:moving_index+14]
        print(window)

        if len(set(window)) == len(window):
            start_of_package_found = True

        moving_index += 1

    chars = datastream[:datastream.index(window)+14]
    char_processed = len(chars)
    print(chars)
    print(char_processed)

    return char_processed


if __name__ == '__main__':
    print("===============")
    print("Advent of Code")
    print("     Day 6    ")
    print("===============\n")

    characters_processed = calculate_start_of_packet_markers("input.txt")
    print("characters processed: ", characters_processed)
