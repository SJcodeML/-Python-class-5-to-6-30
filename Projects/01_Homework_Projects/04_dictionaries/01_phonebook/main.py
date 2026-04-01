# ## Problem Statement

# # In this program we show an example of using dictionaries to keep track of information in a phonebook.



# def read_phone_numbers():
#     """
#     Ask the user for names/numbers to story in a phonebook (dictionary).
#     Returns the phonebook.
#     """
#     phonebook = {}                   # Create empty phonebook

#     while True:
#         name = input("Enter your Name to add in the phonebook or press enter to 'exit': ")
#         if name == "":
#             break
#         number = input("Number: ")
#         phonebook[name] = number

#     return phonebook
   

# def phonebook_print(phonebook):
#     "when user press the enter button.. print the phonebook"
#     for key , value in phonebook.items() :
#        print ("All the user and their phonenumbers "  + key + "->" + value)


# def lookup_number(phonebook):
#     "Ask the user about the name then print the number associated with that name "
#     while True :   
#         user_name = input ("Enter your name to lookup in the dictionary or press enter to exit ")
#         if user_name == "":
#             break 
#         if user_name not in phonebook :
#             print ("Invalid name ")    
#         else:
#             print(f"Your search entry " + phonebook[user_name])    
        





# def main():
#     phonebook = read_phone_numbers()
#     all_contacts =  phonebook_print(phonebook)
#     lookup_number(phonebook)



# if __name__ == "__main__":
#     main()






def read_phone_numbers():
    """
    Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}                    # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number
    
    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


# Python boilerplate.
if __name__ == '__main__':
    main()
