"""This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the 
information.

An example run of the program looks like this (user input is in blue):"""



user_numbers =  []
while True:
    number = input ("Enter a number ")
    user_numbers.append(number)
    print(user_numbers)
    
    

for key in user_numbers:
    print(f"{key} appears {user_numbers.count(key)} times")



def main():
    print("Hello from 00-count-nums!")


if __name__ == "__main__":
    main()
