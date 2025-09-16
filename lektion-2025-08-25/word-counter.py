#!/usr/bin/python3
# This program counts the number of words in a text file.
# User provides the text file.

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            file_content = file.read()
            # if the file is empty return 0 word
            if not file_content:
                return 0

            # Split the content by whitespace to get a list of words and return the count.
            words = file_content.split()
            return len(words)

    except FileNotFoundError:
        raise FileNotFoundError(f"ERROR: The file '{filename}' was not found")


def main():
    # Main function to handle user interaction and file processing.
    filename = input("Please enter the name of the file: ")

    try:
        word_count = count_words_in_file(filename)
        # Display result to user
        print(f"The file '{filename}' contains {word_count} words.")

    except FileNotFoundError as e:
        # Catch and display the specific error message for a missing file.
        print(e)
    
    except Exception as e:
        # Catch any other unexpected errors during file handling.
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
