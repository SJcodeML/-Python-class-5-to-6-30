





def main ():
    try:
        user_year = int(input("Please enter year?  ")) 
    except ValueError:
        print("Invalid year")
        return

    if (user_year % 4 == 0  and user_year % 100 != 0 ) or (user_year % 400 == 0 ):
        print("That's  a leap year")
    else :
        print("That's not a leap year")    




if __name__ == "__main__":
    main()        