Peturksbouipo : int = 16
Stanlau : int = 25 
Mayengua : int = 48




def main():
    try:
       user_question = int(input("What is your age?   "))
    
    except ValueError:
        print("Please enter a valid number for your age.")
        return

    if user_question >= Peturksbouipo:
        print("You can vote in Peturksbouipo where the voting age " +str (Peturksbouipo) + (".")) 
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(Peturksbouipo) + ("."))     
    if user_question >= Stanlau:
        print("You can vote in Stanlau where the voting age is " + str(Stanlau) + ("."))
    else:  
        print("You cannot vote in Stanlau where the voting age is " + str(Stanlau) + ("."))
    if user_question >= Mayengua:
        print("You can vote in Mayengua where the voting age is " + str(Mayengua))
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(Mayengua) + ("."))        

# -----------------------------     
        

# -----------------------------


# PETURKSBOUIPO_AGE : int = 16
# STANLAU_AGE : int = 25
# MAYENGUA_AGE : int = 48

# def main():
#     # Get the user's age
#     user_age = int(input("How old are you? "))

#     # Check if the user can vote in Peturksbouipo
#     if user_age >= PETURKSBOUIPO_AGE:
#         print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
#     else:
#         print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    
#     # Check if the user can vote in Stanlau
#     if user_age >= STANLAU_AGE:
#         print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
#     else:
#         print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    
#     # Check if user can vote in Mayengua
#     if user_age >= MAYENGUA_AGE:
#         print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
#     else:
#         print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")


if __name__ == "__main__":
    main()
