#!/usr/bin/python3

import sys

def read_file(input_filename):
    expressions = []
    try:
        print("Reading calculations from file!")
        with open(input_filename, 'r', encoding='utf-8') as in_file:
            for equation in  in_file:
                expressions.append(equation)
            
                if not expressions:
                    continue # skip empty lines
        
        return expressions

   
    except FileNotFoundError:
        print("Error: No files found")
        sys.exit(1)

    except Exception as e:
        # Handle any other file I/O errors.
        print(f"An error occurred while handling the files: {e}")
        sys.exit(1)


def process_files(input_file_name, output_file_name):
    print("Processing equations from file!")
    equations = read_file(input_file_name)
    try:
        # # Open the output file for writing.
        with open(output_file_name, "w") as out_file:
            for equation in equations:
                try:
                                              
                    results = eval(equation)
                    out_file.write(f"Calculation - {equation}\n")
                    out_file.write(f"Result = {results}\n")
                    out_file.write("-" * 20 + "\n")

                except ZeroDivisionError:
                    # handle division by zero
                    out_file.write(f"Calculation - {equation}")
                    out_file.write("Error: ZeroDivisionError - Cannot divide by zero.\n\n")
                    out_file.write("-" * 20 + "\n")

                except (ValueError, SyntaxError, NameError):
                    # Handles other types of erros
                    # non numeric input (e.g trying to add string)
                    out_file.write(f"Calculation - {equation}")
                    out_file.write("Error: Invalid expression or type error\n")
                    out_file.write("-" * 20 + "\n")
                
                except Exception as e:
                    # Catch other unexpected errors
                    out_file.write(f"Calculation - {equation}\n")
                    out_file.write(f"An unexpected error occurred: {e}\n")
                    out_file.write("-" * 20 + "\n")

    except Exception as e:
        # Catch other unexpected errors
        out_file.write(f"An unexpected error occurred: {e}\n")
        out_file.write("-" * 20 + "\n")

    print(f"Calculations completed. Results saved to {output_file_name}")





def main():
    # Define the file names.
    input_calculation_list = "to-be-calculated-list.txt"
    output_calculation_result_list = "calculated_result.txt"

    # Run the main function
    process_files(input_calculation_list, output_calculation_result_list)


# Execute main file
if __name__ == "__main__": 
    main()

