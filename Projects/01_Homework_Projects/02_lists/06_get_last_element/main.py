""" Problem Statement: Fill out the function get_last_element(lst) which takes in a list lst as a parameter and 
prints the last element in the list. The list is guaranteed to be
 non-empty, but there are no guarantees on its length."""


def user_prompt():
    entry = []
    prompt  = input("Please type your element here ")
    while prompt != "":
       entry.append(prompt)
       prompt  = input("Please type your element here ")
    return entry


def get_last_element(list_of_elements):
    print(list_of_elements[-1])
 
def main():
    element = user_prompt() 
    get_last_element(element)



if __name__ == "__main__":
    main()
