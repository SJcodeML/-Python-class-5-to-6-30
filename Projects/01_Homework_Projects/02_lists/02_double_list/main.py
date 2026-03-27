## Problem Statement

# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

def double_numbers(numbers:list)-> list:
   
    return [x * 2 for x in numbers]

def main():
    
   numbers = [1, 2, 3, 4]
   result = double_numbers(numbers)
   print(result)

if __name__ == "__main__":
    main()
