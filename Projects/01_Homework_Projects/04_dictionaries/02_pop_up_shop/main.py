# ## Problem Statement

# # There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs. 

# # Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# # Here is an example run of the program (user input is in bold italics):

# # How many (apple) do you want?: 2

# # How many (durian) do you want?: 0

# # How many (jackfruit) do you want?: 1

# # How many (kiwi) do you want?: 0

# # How many (rambutan) do you want?: 1

# # How many (mango) do you want?: 3

# # Your total is $99.5




# fruits = {
#     "apple":2,
#     "durian":3,
#     "jackfruit":5,
#     "kiwi":10,
#     "rambutan":5,
#     "mango":11, 
#     }

# def fruit_shop(furits):
#     total_cost = 0
#     for fruit_name in fruits:
        
#         price = fruits[fruit_name]
#         user_input = int(input (f"Enter your desired quantity of {fruit_name}: "))
#         total_cost += (price *user_input)


#     print("your total cost is " + str(total_cost))

# def main():
#     print(fruit_shop(fruits))


# if __name__ == "__main__":
#     main()


























def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    total_cost = 0

    for fruit_name, price in fruits.items():
        while True:
            s = input(f"How many ({fruit_name}) do you want to buy?: ").strip()
            if s == "":
                print("Please enter a number (cannot be empty).")
                continue
            try:
                amount_bought = int(s)
                if amount_bought < 0:
                    print("Please enter 0 or a positive number.")
                    continue
                break
            except ValueError:
                print("Please enter a whole number (e.g., 0, 1, 2...).")

        total_cost += price * amount_bought

    print("Your total is $" + str(total_cost))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()