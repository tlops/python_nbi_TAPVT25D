#!/usr/bin/python3

import sys

def read_file(input_filename):
    print("Reading calculations from file")
    open(input_filename, 'r', encoding='utf-8') 
    for equation, line in  enumerate(infile, 1):
        expression = line.strip()
    return expression

 #   try:
 #      with open(input_filename, 'r', encoding='utf-8') as infile:
 #           for equation, line in  enumerate(infile, 1): 
 #               expression = line.strip()

  #          return expression
   
  # except:
   #     print("No files found - startar med en tom lista")
    #    return []


def main():
    file_name = "to-be-calculated-list.txt"
    equations = read_file(file_name)
    for equation in equations:
        print(f" - {equation}")





if __name__ == "__main__": 
    main()