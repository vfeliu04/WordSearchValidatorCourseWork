# Word Search Puzzle Checker (COMP 1012 Coursework 1)

This repository contains my submission for the COMP 1012 coursework assignment. The project implements a word search puzzle checker in Python, which validates puzzles and identifies word locations without using external modules.

## Description

The word search puzzle checker verifies the validity of word search grids and lists of words, displaying the grid with highlighted words if they are found. The program handles various orientations and positions of the words within the grid.

### Features

- **Validation of Word Search Puzzles**: Ensures all rows in the puzzle are of the same length and only contain strings.
- **Validation of Word Lists**: Checks if the provided word list contains valid strings.
- **Display Functions**: Basic and colored display outputs for visual verification of the puzzle and found words.
- **Multi-Position Search**: Identifies multiple positions and orientations of words within the grid.
- **Error Handling**: Provides feedback if the word or puzzle is invalid.

## Installation

No installation is necessary, other than having Python installed on your system. This program was developed with Python and follows PEP 8 standards.

## Usage

1. Download the repository to your local system.
2. Run the script from your terminal:

```
python wordsearch.py
```

## Example

Here's how to use the program with an example puzzle and word list:
```
python wordsearch.py --puzzle your_puzzle_file.txt --words your_word_list.txt
```
Replace your_puzzle_file.txt and your_word_list.txt with paths to your actual files.

## Contributing

Given this project is part of a university coursework, I do not take 100% ownership of the code.
