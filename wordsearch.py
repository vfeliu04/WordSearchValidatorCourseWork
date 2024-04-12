"""
Introduction to Programming: Coursework 1
Please write your name
@author: Vicente Maria Feliu

"""


# Reminder: You are not allowed to import any modules.


def wordsearch(puzzle: list, wordlist: list) -> None:
    # If the puzzle is valid and the wordlist is valid then create an array
    # called positions
    if valid_puzzle(puzzle) and valid_wordlist(wordlist):
        positions = []
        # Loop through the wordlist and add to the list position the
        # coordinates of the word in the puzzle
        for item in wordlist:
            positions.append(get_positions(puzzle, item))
        # Call the function coloured_display
        coloured_display(puzzle, positions)
    # If the puzzle or wordlist is not valid returns error
    else:
        return "ValueError, invalid puzzle or wordlist"


def valid_puzzle(puzzle: list) -> bool:
    length_of_word = 0
    one_timer = 0
    checker = 0
    # Searching word in puzzle
    for word in puzzle:
        # Setting a one time check to get the length of the first word inside
        # puzzle
        if one_timer == 0:
            length_of_word = len(word)
            one_timer += 1
        # Checking if the word fits the standard and if it does add 1 to the
        # checker if it does not fit return false
        if length_of_word == len(word) and isinstance(word, str):
            word.upper()
            checker += 1
        else:
            return False
    # If the number of checker is the same as the number of words inside the
    # puzzle then it returns true
    if checker == len(puzzle):
        return True


def valid_wordlist(wordlist: list) -> bool:
    # Loop through the word in the wordlist and if it is not a string return
    # false
    for word in wordlist:
        if not isinstance(word, str):
            return False
    return True


def get_positions(puzzle: list, word: str) -> list:
    # A counter in order to keep track of the characters within the word
    character_counter = 0
    # To store the coordinates of the word
    location = []
    # To store characters and later word in order to compare them to the
    # word later
    character = []
    test_word = ""

    # Boolean found in order to state if the word was found or not
    found = False

    # Defining the limit of the puzzle
    horizontal_limit = len(puzzle) - 1
    vertical_limit = len(puzzle[0]) - 1

    # Making sure that the word is in upper case letter
    word = word.upper()

    # Loop through strings of the puzzle
    for horz in range(len(puzzle)):
        # Loop through the characters of the string
        for vert in range(len(puzzle[horz])):
            # If the current character of the string of the puzzle is
            # equal to the first character of the word then...
            if puzzle[horz][vert] == word[character_counter]:

                # Add the character to the character list
                character.append(puzzle[horz][vert])

                # Add one to the character_counter
                character_counter += 1

                # Add the current coordinates of the character to
                # the location list
                location.append([horz, vert])

                # Crate two temporary variables to store the current
                # value of the coordinates
                temp_horz = horz
                temp_vert = vert

                # Direction moving: below
                # If the character below the current one is less or equal to
                # the limit and it is equal to the
                # current character of the word then...
                if (horz + 1 <= horizontal_limit) and \
                        puzzle[horz + 1][vert] == word[character_counter]:
                    # Add one to the horz
                    horz += 1

                    # Add the current character in the string of the puzzle
                    # to the character list
                    character.append(puzzle[horz][vert])

                    # Add the current coordinates to the location list
                    location.append([horz, vert])

                    # Add one to the character_counter
                    character_counter += 1

                    # While the character_counter is not equal to the length
                    # of the word and the horz plus one value is
                    # not over the horizontal limit and the character below
                    # in the puzzle is equal to the currenct
                    # character in the word
                    while (not character_counter == len(word)) and (
                            horz + 1 <= horizontal_limit) and (
                            puzzle[horz + 1][vert] == word[character_counter]):
                        # Add one to the horz value
                        horz += 1

                        # Add the current character of the puzzle to the
                        # character list
                        character.append(puzzle[horz][vert])

                        # Add the coordinates of the character to the
                        # location list
                        location.append([horz, vert])

                        # Add one to the character counter
                        character_counter += 1

                    # If all the characters joined in the character list
                    # is equal to the word we are looking for then...
                    if test_word.join(character) == word:
                        # Convert the location list to a tuple and
                        # att it to the final list
                        final = tuple(location)
                        return final
                    else:
                        # Set the character counter to original
                        character_counter -= 1

                        # Delete the last coordinates of the location list
                        del location[-1]

                        # Delete the last character in the character list
                        del character[-1]

                        # Set the horz and vert value back to original
                        horz = temp_horz
                        vert = temp_vert

                # Direction moving: above
                # This block of code has the same function as the first one
                # therefore will not include specific
                # comments.The only difference is that this block of code
                # looks at the character above the current one
                if (horz - 1 >= 0) and puzzle[horz - 1][vert] == word[
                        character_counter]:
                    horz -= 1
                    character.append(puzzle[horz][vert])
                    location.append([horz, vert])
                    character_counter += 1
                    while (not character_counter == len(word)) and (
                            horz - 1 >= 0) and (
                            puzzle[horz - 1][vert] == word[character_counter]):
                        horz -= 1
                        character.append(puzzle[horz][vert])
                        location.append([horz, vert])
                        character_counter += 1
                    if test_word.join(character) == word:
                        final = tuple(location)
                        return final
                    else:
                        character_counter -= 1
                        del location[-1]
                        del character[-1]
                        horz = temp_horz
                        vert = temp_vert

                # Direction moving: left
                # This block of code has the same function as the first one
                # therefore will not include specific
                # comments.The only difference is that this block of code looks
                # at the character left the current one
                if (vert - 1 >= 0) and puzzle[horz][vert - 1] == word[
                        character_counter]:
                    vert -= 1
                    character.append(puzzle[horz][vert])
                    location.append([horz, vert])
                    character_counter += 1
                    while (not character_counter == len(word)) and (
                            vert - 1 >= 0) and (
                            puzzle[horz][vert - 1] == word[character_counter]):
                        vert -= 1
                        character.append(puzzle[horz][vert])
                        location.append([horz, vert])
                        character_counter += 1
                    if test_word.join(character) == word:
                        final = tuple(location)
                        return final
                    else:
                        character_counter -= 1
                        del location[-1]
                        del character[-1]
                        horz = temp_horz
                        vert = temp_vert

                # Direction moving: right
                # This block of code has the same function as the first one
                # therefore will not include specific
                # comments.The only difference is that this block of code
                # looks at the character right the current one
                if (vert + 1 <= vertical_limit) and puzzle[
                        horz][vert + 1] == word[character_counter]:
                    vert += 1
                    character.append(puzzle[horz][vert])
                    location.append([horz, vert])
                    character_counter += 1
                    while (not character_counter == len(word)) and (
                            vert + 1 <= vertical_limit) and (
                            puzzle[horz][vert + 1] == word[character_counter]):
                        vert += 1
                        character.append(puzzle[horz][vert])
                        location.append([horz, vert])
                        character_counter += 1
                    if test_word.join(character) == word:
                        final = tuple(location)
                        return final
                    else:
                        character_counter -= 1
                        del location[-1]
                        del character[-1]
                        horz = temp_horz
                        vert = temp_vert

                # Direction moving: right upper corner
                # This block of code has the same function as the first one
                # therefore will not include specific
                # comments.The only difference is that this block of code
                # looks at the character to the right upper
                # corner the current one
                if (horz - 1 >= 0) and (vert + 1 <= vertical_limit) and \
                        puzzle[horz - 1][vert + 1] == word[character_counter]:
                    vert += 1
                    horz -= 1
                    character.append(puzzle[horz][vert])
                    location.append([horz, vert])
                    character_counter += 1
                    while (not character_counter == len(word)) and (
                            horz - 1 >= 0) and (vert + 1 <= vertical_limit
                                                ) and (puzzle[horz - 1][
                                                    vert + 1] == word[
                                                        character_counter]):
                        vert += 1
                        horz -= 1
                        character.append(puzzle[horz][vert])
                        location.append([horz, vert])
                        character_counter += 1
                    if test_word.join(character) == word:
                        final = tuple(location)
                        return final
                    else:
                        character_counter -= 1
                        del location[-1]
                        del character[-1]
                        horz = temp_horz
                        vert = temp_vert

                # Direction moving: left upper corner
                # This block of code has the same function as the first one
                # therefore will not include specific
                # comments.The only difference is that this block of code
                # looks at the character to the left upper
                # corner the current one
                if (horz - 1 >= 0) and (vert - 1 >= 0) and puzzle[horz - 1][
                        vert - 1] == word[character_counter]:
                    vert -= 1
                    horz -= 1
                    character.append(puzzle[horz][vert])
                    location.append([horz, vert])
                    character_counter += 1
                    while (not character_counter == len(word)) and \
                        (horz - 1 >= 0) and (vert - 1 >= 0) and (
                            puzzle[horz - 1][vert - 1] ==
                            word[character_counter]):
                        vert -= 1
                        horz -= 1
                        character.append(puzzle[horz][vert])
                        location.append([horz, vert])
                        character_counter += 1
                    if test_word.join(character) == word:
                        final = tuple(location)
                        return final
                    else:
                        character_counter -= 1
                        del location[-1]
                        del character[-1]
                        horz = temp_horz
                        vert = temp_vert

                # Direction moving: right lower corner
                # This block of code has the same function as the first one
                # therefore will not include specific
                # comments.The only difference is that this block of
                # code looks at the character to the right lower
                # corner the current one
                if (horz + 1 <= horizontal_limit) and (
                        vert + 1 <= vertical_limit) and puzzle[
                            horz + 1][vert + 1] == \
                        word[character_counter]:
                    vert += 1
                    horz += 1
                    character.append(puzzle[horz][vert])
                    location.append([horz, vert])
                    character_counter += 1
                    while (not character_counter == len(word)) and (
                            horz + 1 <= horizontal_limit) and (
                            vert + 1 <= vertical_limit) and (
                                puzzle[horz + 1][vert + 1] ==
                                word[character_counter]):
                        vert += 1
                        horz += 1
                        character.append(puzzle[horz][vert])
                        location.append([horz, vert])
                        character_counter += 1
                    if test_word.join(character) == word:
                        final = tuple(location)
                        return final
                    else:
                        character_counter -= 1
                        del location[-1]
                        del character[-1]
                        horz = temp_horz
                        vert = temp_vert

                # Direction moving: left lower corner
                # This block of code has the same function as the first one
                # therefore will not include specific comments.The only
                # difference is that this block of code looks at the character
                # to the left lower corner the current one
                if (horz + 1 <= horizontal_limit) and (vert - 1 >= 0) and \
                        puzzle[horz + 1][vert - 1] == word[character_counter]:
                    vert -= 1
                    horz += 1
                    character.append(puzzle[horz][vert])
                    location.append([horz, vert])
                    character_counter += 1
                    while (not character_counter == len(word)) and \
                        (horz + 1 <= horizontal_limit) and (
                            vert - 1 >= 0) and \
                            (puzzle[horz + 1][vert - 1]
                             == word[character_counter]):
                        vert -= 1
                        horz += 1
                        character.append(puzzle[horz][vert])
                        location.append([horz, vert])
                        character_counter += 1
                    if test_word.join(character) == word:
                        final = tuple(location)
                        return final
                    else:
                        character_counter -= 1
                        del location[-1]
                        del character[-1]
                        horz = temp_horz
                        vert = temp_vert

                # If the second character of the word we are looking for is
                # not in the surrounding of the first letter
                else:

                    # Reset all variables to their original value
                    character_counter = 0
                    location = []
                    character = []
                    horz = temp_horz
                    vert = temp_vert

    # If the word is not found then...
    if not found:

        # Return that the word was not found
        return "'" + word + "'" + " not found"


def basic_display(grid: list) -> None:

    # Search through the word in the grid
    for word in grid:
        # Search through the character of the word
        for character in word:

            # Make the character upper case and print the character with
            # a space in between
            character = character.upper()
            print(character, end=" ")
        print("")


def coloured_display(grid: list, positions: list) -> None:
    # Create a new list
    new_list = []

    # Search through the tuples in the list
    for outer in range(len(positions)):

        # Convert the positions[outer] into list from tuples
        positions[outer] = list(positions[outer])

        # Search through the list in the outer
        for inner in range(len(positions[outer])):
            # Add all the coordinates to a new list
            new_list.append(positions[outer][inner])

    # Arrange the list of coordinates from lowest to highest and if they
    # have the same initial value arrange it
    # according to the secondary value
    arranged_list = sorted(new_list, key=lambda x: (x[0], x[1]))

    # Loop through the list within the arranged list
    for outers in range(len(arranged_list)):
        # If the next value of the list is less than the length of the
        # list and the current value is equal to
        # the next value
        if (outers + 1 < len(arranged_list)) and (arranged_list[outers] ==
                                                  arranged_list[outers + 1]):

            # Delete the repeated value
            del (arranged_list[outers])

    # Create variables that will be used to access the arranged list
    first = 0
    second = 0

    # Loop through the words of the grid
    for horz in range(len(grid)):

        # Loop through the character of the words of the grid
        for vert in range(len(grid[horz])):

            # If the first character is smaller than the length of the
            # first list and the current grid vlaue is equal
            # to the current value of the arranged list then...
            if first < len(arranged_list) and \
                horz == arranged_list[first][second] and \
                    vert == arranged_list[first][second + 1]:

                # Print the value of the grid with a green background
                print("\033[42m" + grid[horz][vert] + "\033[0m", end=" ")

                # Add one to the first value
                first += 1
            else:

                # Print the value of the grid normally
                print(grid[horz][vert], end=" ")
        print("")


# =============================================================================
# Do not remove the followings. To test your functions
# =============================================================================


def test_valid_wordlist():
    """
    Test function valid_wordlist()
    """
    good_wordlist = ["scalar", "tray", "blew", "sevruc", "testing"]
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    bad_wordlist2 = ["scalar", "tray", "blew", "sevruc", 59]

    print("wordlist is", valid_wordlist(good_wordlist))
    print("wordlist is", valid_wordlist(good_wordlist2))
    print("wordlist is", valid_wordlist(bad_wordlist2))


def test_valid_puzzle():
    good_puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle1 = ['RUNAROUNDDL', 'EDCITOAHC', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle2 = ['RUNAROUNDDL', ['EDCITOAHCYV'], ('ZYUWSWEDZYA'),
                   'AKOTCONVOYV', 'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL',
                   'ISTREWZLCGY', 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    print("puzzle is", valid_puzzle(good_puzzle))
    print("puzzle is", valid_puzzle(bad_puzzle1))
    print("puzzle is", valid_puzzle(bad_puzzle2))


def test_basic_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    basic_display(puzzle1)
    basic_display([['a', 'b', 'c', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    get_positions(puzzle1, "TESTING")
    print(get_positions(puzzle1, "LET"))


def test_coloured_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    final_list = []
    for word in good_wordlist2:
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    coloured_display(puzzle1, final_list)


def test_wordsearch():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    wordsearch(puzzle1, good_wordlist2)


if __name__ == "__main__":
    # uncomment the test function individually
    # basic solution
    # test_valid_puzzle()
    # test_valid_wordlist()
    # test_basic_display()

    # full solution
    # test_coloured_display()
    # test_get_positions()
    test_wordsearch()
