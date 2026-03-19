


#printing the list 
def print_the_list (list_of_elements):
    print(list_of_elements)


def get_elements_for_list():
    values = []
    elem = input("Please enter your value and just press enter to stop the program  ")
    while elem != "":
        values.append(elem)
        elem = input("Please enter your value and just press enter to stop the program  ")
    return values    
        



def main():
    value = get_elements_for_list()
    print_the_list(value)






if __name__ == "__main__":
    main()
