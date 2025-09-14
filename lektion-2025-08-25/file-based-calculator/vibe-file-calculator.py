# This program reads arithmetic expressions from a file,
# evaluates them, and saves the results to a new file.

import sys

def calculate_from_file(input_filename, output_filename):
    """
    Reads arithmetic expressions from an input file, handles errors,
    and writes the results to an output file.

    Args:
        input_filename (str): The name of the file containing the expressions.
        output_filename (str): The name of the file to save the results to.
    """
    try:
        # Open the input file for reading.
        with open(input_filename, 'r', encoding='utf-8') as infile:
            # Open the output file for writing.
            with open(output_filename, 'w', encoding='utf-8') as outfile:
                # Iterate through each line in the input file.
                for line_number, line in enumerate(infile, 1):
                    # Clean up the line by removing leading/trailing whitespace.
                    expression = line.strip()
                    
                    if not expression:
                        continue # Skip empty lines.

                    try:
                        # Use eval() to perform the calculation.
                        # This function is powerful but can be risky with untrusted input.
                        # For this specific task, it's suitable.
                        result = eval(expression)
                        # Write the expression and the successful result to the output file.
                        outfile.write(f"Calculation: {expression}\n")
                        outfile.write(f"Result: {result}\n")
                        outfile.write("-" * 20 + "\n")
                    except ZeroDivisionError:
                        # Handle division by zero.
                        outfile.write(f"Calculation: {expression}\n")
                        outfile.write("Error: ZeroDivisionError - Cannot divide by zero.\n")
                        outfile.write("-" * 20 + "\n")
                    except (ValueError, SyntaxError, NameError):
                        # Handle other types of errors, such as invalid syntax or
                        # non-numeric input (e.g., trying to add a string).
                        outfile.write(f"Calculation: {expression}\n")
                        outfile.write("Error: Invalid expression or type error.\n")
                        outfile.write("-" * 20 + "\n")
                    except Exception as e:
                        # Catch any other unexpected errors.
                        outfile.write(f"Calculation: {expression}\n")
                        outfile.write(f"An unexpected error occurred: {e}\n")
                        outfile.write("-" * 20 + "\n")

    except FileNotFoundError:
        # Handle the case where the input file does not exist.
        print(f"Error: The file '{input_filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        # Handle any other file I/O errors.
        print(f"An error occurred while handling the files: {e}")
        sys.exit(1)

    print(f"Calculations completed. Results saved to '{output_filename}'.")

if __name__ == "__main__":
    # Define the file names.
    input_file_name = "to-be-calculated-list.txt"
    output_file_name = "vibe_result-file.txt"
    
    # Run the main function.
    calculate_from_file(input_file_name, output_file_name)
