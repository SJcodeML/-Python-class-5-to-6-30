










"""
Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item 
it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged.
We've written a main() function for you which gets a list and passes it into your function once you run the program.
For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program."""




def get_elements_for_list():
    values = []
    elem = input("Enter your values here ")
    while elem != "" : 
        values.append(elem)
        elem = input("Enter your values here ")

    return values     

def shorten_the_length (list_of_elements):
    max_length: int = 3
    while len(list_of_elements) > max_length:
        `popped_value` = list_of_elements.pop()
        print(popped_value)
            
    
        
def main():
    question = get_elements_for_list()
    shorten_the_length(question)


if __name__ == "__main__":
    main()
