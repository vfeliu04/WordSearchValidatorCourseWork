if __name__ == "__main__":

    # Open the file then create a list and while there is a line to read add that line to the list
    with open('word_list.txt') as f:
        word_list = []
        while True:
            line = f.readline().upper()
            if not line:
                break
            word_list.append(line.strip())

    # Open the file then create a list and while there is a line to read add that line to the list
    with open('characters_list.txt') as f:
        characters_list = []
        while True:
            line = f.readline().upper()
            if not line:
                break
            characters_list.append(line.strip())

    print(characters_list)

    print("You can now decide the size of your grid... eg 12x12")
    # Since random can not be imported then the random numbers must come from the user
    size = int(input("What size do you want the grid to be (number less than 21 but more than 10): "))
    # Perform a check in order to see if the size is vaiable or not
    if 21 > int(size) > 10:
        # Create the grid of range size given by the user and fill it with 0s
        grid = [[0 for i in range(size)] for j in range(size)]

        # Asking the user to input two random numbers in order to mark the starting location of the first word
        starting_horz = int(input("Input random number less than " + str(size) + ": "))
        starting_vert = int(input("Input another random number less than " + str(size) + ": "))
        # Number of words which will be inputed into the grid
        num_of_word = int(size / 5)
        # Starting word from the word_list
        starting_word = int(input("Input another random number less than " + str(num_of_word - 1000) + ": "))
        # Checking that the number given by the user is wtihin the limit of the grid
        if (startin_index < size) and (starting_vert < size) and ((num_of_word - 1000) < starting_word):
            # Loop through the chosen_word list in order to get each individual word
            for word in range(len(chosen_word)):
                # Take note of the current length of the word
                word_length = len(choesn_word[word])
                # Check if the horizontal location minus the word length is not less than zero
                if not((starting_horz - word_length) < 0):
                    # If this is true then the word can be put in upwards direction
                    # Loop through the characters of the word
                    for chars in range(len(chosen_word[word])):
                        # Replace the current place in the grid with the character of the word
                        grid[starting_horz][starting_vert] = word_chosen[word][chars]
                        # Add one to the starting horizontal of the grid
                        starting_horz += 1
                    # Once done check if the next vertical location is below limit and add one else take away one
                    if (starting_vert + 1) > 20:
                        starting_vert += 1
                    else:
                        startin_vert -= 1

        # Loop through the grid and if the current grid index is 0 then repalce it with a cahracter form the list.
        for horz in range(len(grid)):
            for vert in range(len(grid[horz])):
                if grid[horz][vert] == 0:
                    counter = counter + 1
                    grid[horz][vert] = characters_list[counter]

        for item in grid:
            for i in item:
                print(i, end=" ")
            print("")