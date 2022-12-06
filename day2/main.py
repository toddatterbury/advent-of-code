

def calculate_score(filename):

    with open('input.txt') as f:
        lines = f.readlines()

    # Track points
    total_points = 0
    for line in lines:
        elf, me = line.split(' ')
        me = me[0]  # Get rid of \n character
        print('Elf: ', elf, 'Me: ', me)

        # Track points
        points = 0

        # Calculate points based on move made
        if me == 'X':
            points += 1     # Rock
        elif me == 'Y':
            points += 2     # Paper
        elif me == 'Z':
            points += 3     # Scissors

        # Calculate points based on outcome of game

        # Elf plays ROCK
        if elf == 'A':
            if me == 'X':
                points += 3     # Rock
            elif me == 'Y':
                points += 6     # Paper
            elif me == 'Z':
                points += 0     # Scissors

        # Elf plays PAPER
        elif elf == 'B':
            if me == 'X':
                points += 0     # Rock
            elif me == 'Y':
                points += 3     # Paper
            elif me == 'Z':
                points += 6     # Scissors

        # Elf plays SCISSORS
        elif elf == 'C':
            if me == 'X':
                points += 6     # Rock
            elif me == 'Y':
                points += 0     # Paper
            elif me == 'Z':
                points += 3     # Scissors

        total_points += points

    return total_points


def calculate_score_part2(filename):

    with open('input.txt') as f:
        lines = f.readlines()

    # Track points
    total_points = 0
    for line in lines:
        elf, result = line.split(' ')
        result = result[0]  # Get rid of \n character
        print('Elf: ', elf, 'Result: ', result)

        # Track points
        points = 0

        # LOSE
        if result == 'X':

            # Elf plays ROCK
            if elf == 'A':
                # Play scissors
                points += 3     # Scissors
                points += 0     # Lose

            # Elf plays PAPER
            elif elf == 'B':
                # Play rock
                points += 1     # Rock
                points += 0     # Lose

            # Elf plays SCISSORS
            elif elf == 'C':
                # Play Paper
                points += 2     # Paper
                points += 0     # Lose

        # DRAW
        if result == 'Y':

            # Elf plays ROCK
            if elf == 'A':
                # Play ROCK
                points += 1  # ROCK
                points += 3  # Draw

            # Elf plays PAPER
            elif elf == 'B':
                # Play PAPER
                points += 2  # PAPER
                points += 3  # Draw

            # Elf plays SCISSORS
            elif elf == 'C':
                # Play SCISSORS
                points += 3  # SCISSORS
                points += 3  # Draw

        # WIN
        if result == 'Z':

            # Elf plays ROCK
            if elf == 'A':
                # Play Paper
                points += 2  # Paper
                points += 6  # Win

            # Elf plays PAPER
            elif elf == 'B':
                # Play rock
                points += 3  # Scissors
                points += 6  # Win

            # Elf plays SCISSORS
            elif elf == 'C':
                # Play Paper
                points += 1  # Rock
                points += 6  # Win

        total_points += points

    return total_points


if __name__ == '__main__':
    print("===============")
    print("Advent of Code")
    print("     Day 2    ")
    print("===============\n")

    total_score = calculate_score_part2("input.txt")
    print("Total: ", total_score)
