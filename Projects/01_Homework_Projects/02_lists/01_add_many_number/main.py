# Write a function that takes a list of numbers and returns the sum of those numbers.



# def total_number(numbers:list):
#      """
#     Takes in a list of numbers and returns the sum of those numbers.
#     """
#      return sum(numbers)


# def main():
#     numbers = [1 , 2 , 3 , 4 , 5]
#     sum_of_number = total_number(numbers)
#     print(sum_of_number)


# if __name__ == "__main__":
#     main()





#  ------------------------------------------------------

# taking list of numbers from user and calculating the sum of those numbers



def total_number(numbers):
    return sum(numbers)

def main():
    # Read a line of space-separated numbers, e.g.,: "1 2 3 4"
    line = input("Write your numbers here (space-separated): ")
    try:
        numbers = [int(x) for x in line.strip().split()]
    except ValueError:
        print("Invalid Number")
        return

    result = total_number(numbers)
    print("Sum:", result)

if __name__ == "__main__":
    main()


'''Explanation of the code 


Here's what that line does, step by step:

- It assumes there is a variable called line that contains a string, typically entered by the user (for example: "1 2 3 4").

- line.strip(): removes leading and trailing whitespace (spaces, tabs, newlines) from the string without changing the interior.

- line.strip().split(): splits the trimmed string into a list of substrings using whitespace as the default delimiter. For example, "1 2 3" becomes ["1", "2", "3"].

- [x for x in line.strip().split()]: this is a list comprehension that iterates over each substring produced by split(), collecting them into a new list. After the split, you effectively have a list of numeric strings, like ["1", "2", "3"].

- int(x) for x in ...: inside the list comprehension, each substring x is converted to an integer using int(x). So "1" becomes 1, "2" becomes 2, etc.

- The entire expression [int(x) for x in line.strip().split()] thus yields a list of integers corresponding to the numbers written in the original line. For example, input "  4  15  9 " would produce [4, 15, 9].

Common uses:
- Converting a space-separated string of numbers into a list of ints so you can perform numeric operations or pass them to a function.
'''