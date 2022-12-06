
if __name__ == '__main__':
    print("===============")
    print("Advent of Code")
    print("     Day 1    ")
    print("===============\n")

    elfs = []

    with open('input.txt') as f:
        lines = f.readlines()

        count = 0
        for line in lines:

            # If no more calories, add total to list of elfs
            # and reset count
            if line == '\n':
                elfs.append(count)
                count = 0

            # Sum up each value for elf
            else:
                val = line.split('\n')[0]
                count += int(val)

        # Get max total calories
        max1 = max(elfs)

        top3 = 0
        for i in range(3):
            # Find and remove max from list
            maxCount = max(elfs)
            print("Max: ", maxCount)
            top3 += maxCount
            elfs.remove(maxCount)

        print("Top 3: ", top3)
